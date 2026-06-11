"""
Basic Chatbot with LangGraph
"""

# =============================================================================
# IMPORTS
# =============================================================================

import streamlit as st
from langchain_openai import ChatOpenAI
from utils.styles import apply_base_css
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict


# =============================================================================
# PAGE SETUP
# =============================================================================

st.set_page_config(
    page_title="Basic Chatbot",
    page_icon=None,
    layout="centered"
)

apply_base_css()

st.markdown('<div class="page-title">Basic AI Chat</div>', unsafe_allow_html=True)
st.markdown('<div class="page-caption">A friendly AI assistant that chats with you.</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)


# =============================================================================
# SESSION STATE
# =============================================================================

if "llm" not in st.session_state:
    st.session_state.llm = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot" not in st.session_state:
    st.session_state.chatbot = None


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
    <div class="info-banner">OpenAI key loaded from Home — ready to chat.</div>
    """, unsafe_allow_html=True)


# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("**Basic AI Chat**")
    st.caption("Simple LLM conversation with no tools or retrieval.")
    st.divider()
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.session_state.chatbot = None
        st.session_state.llm = None
        st.rerun()
    if st.button("Home"):
        st.switch_page("Home.py")


# =============================================================================
# INITIALIZE AI
# =============================================================================

if not st.session_state.llm:
    st.session_state.llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=openai_key
    )


# =============================================================================
# BUILD CHATBOT GRAPH
# =============================================================================

if st.session_state.llm and not st.session_state.chatbot:

    class State(TypedDict):
        messages: Annotated[list, add_messages]

    def chatbot_node(state: State):
        system_msg = SystemMessage(
            content="You are a helpful and friendly AI assistant. Have natural conversations with users."
        )
        messages = [system_msg] + state["messages"]
        response = st.session_state.llm.invoke(messages)
        return {"messages": [response]}

    workflow = StateGraph(State)
    workflow.add_node("chatbot", chatbot_node)
    workflow.add_edge(START, "chatbot")
    workflow.add_edge("chatbot", END)
    st.session_state.chatbot = workflow.compile()


# =============================================================================
# GREETING
# =============================================================================

if not st.session_state.messages:
    greeting = "Hi! My name is Assistant. What can I do for you today?"
    st.session_state.messages.append({"role": "assistant", "content": greeting})

# =============================================================================
# CHAT HISTORY
# =============================================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# =============================================================================
# USER INPUT
# =============================================================================

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            messages = []
            for msg in st.session_state.messages:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                else:
                    messages.append(AIMessage(content=msg["content"]))

            result = st.session_state.chatbot.invoke({"messages": messages})
            response = result["messages"][-1].content

            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
