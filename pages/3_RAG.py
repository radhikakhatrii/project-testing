"""
Chat with your Data - RAG with PDF documents.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import streamlit as st
import os

from utils.styles import apply_base_css
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


# =============================================================================
# PAGE SETUP
# =============================================================================

st.set_page_config(
    page_title="RAG — Retrieval-Augmented Generation",
    page_icon=None,
    layout="centered"
)

apply_base_css()

st.markdown('<div class="page-title">RAG — Retrieval-Augmented Generation</div>', unsafe_allow_html=True)
st.markdown('<div class="page-caption">Upload PDF documents and ask questions about their content.</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)


# =============================================================================
# SESSION STATE
# =============================================================================

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "rag_llm" not in st.session_state:
    st.session_state.rag_llm = None

if "rag_messages" not in st.session_state:
    st.session_state.rag_messages = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []


# =============================================================================
# CHECK API KEY FROM HOME PAGE
# =============================================================================

openai_key = st.session_state.get("openai_key", "")

if not openai_key:
    st.markdown("""
    <div class="warn-banner">
        No API key found. Please go back to the Home page and save your OpenAI API key first.
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Home"):
        st.switch_page("Home.py")
    st.stop()
else:
    st.markdown("""
    <div class="info-banner">OpenAI key loaded — upload a PDF below to get started.</div>
    """, unsafe_allow_html=True)


# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("**RAG — Retrieval-Augmented Generation**")
    st.caption("Ask questions grounded in your uploaded documents.")
    st.divider()
    if st.button("Clear chat"):
        st.session_state.rag_messages = []
        st.rerun()
    if st.button("Clear documents"):
        st.session_state.vector_store = None
        st.session_state.rag_llm = None
        st.session_state.rag_messages = []
        st.session_state.processed_files = []
        st.rerun()
    if st.button("Home"):
        st.switch_page("Home.py")


# =============================================================================
# PDF UPLOAD AND PROCESSING
# =============================================================================

uploaded_files = st.file_uploader(
    "Upload PDF documents",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    current_files = [f.name for f in uploaded_files]

    if st.session_state.processed_files != current_files:
        with st.spinner("Processing documents..."):
            documents = []
            os.makedirs("tmp", exist_ok=True)

            for file in uploaded_files:
                file_path = os.path.join("tmp", file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getvalue())
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1500,
                chunk_overlap=200
            )
            chunks = text_splitter.split_documents(documents)

            embeddings = OpenAIEmbeddings(api_key=openai_key)
            st.session_state.vector_store = FAISS.from_documents(chunks, embeddings)

            st.session_state.rag_llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
                api_key=openai_key
            )

            st.session_state.rag_messages = []
            st.session_state.processed_files = current_files

        st.success(f"Processed {len(uploaded_files)} document(s). You can now ask questions below.")

st.markdown('<hr class="divider">', unsafe_allow_html=True)


# =============================================================================
# CHAT INTERFACE
# =============================================================================

if st.session_state.vector_store:

    if not st.session_state.rag_messages:
        greeting = "Hi! My name is Assistant. I've read your documents and I'm ready to answer questions about them. What would you like to know?"
        st.session_state.rag_messages.append({"role": "assistant", "content": greeting})

    for message in st.session_state.rag_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Ask a question about your documents...")

    if user_input:
        st.session_state.rag_messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Searching documents..."):
                retriever = st.session_state.vector_store.as_retriever()
                docs = retriever.invoke(user_input)
                context = "\n\n---\n\n".join(doc.page_content for doc in docs[:5])

                if not context.strip():
                    response_text = "I couldn't find relevant information in the uploaded documents."
                else:
                    prompt = ChatPromptTemplate.from_messages([
                        ("system", "Answer the question using ONLY the provided context. Be concise and accurate."),
                        ("human", "Question: {question}\n\nContext: {context}\n\nAnswer:")
                    ])
                    response = st.session_state.rag_llm.invoke(
                        prompt.format_messages(question=user_input, context=context)
                    )
                    response_text = response.content

                st.write(response_text)
                st.session_state.rag_messages.append({
                    "role": "assistant",
                    "content": response_text
                })

else:
    st.info("Upload one or more PDF documents above to start chatting.")
