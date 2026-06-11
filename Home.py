"""
LLM Bootcamp Project - Home Page
"""

import streamlit as st
from utils.styles import apply_home_css

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="LLM Bootcamp Project",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

apply_home_css()

# ============================================================================
# SESSION STATE
# ============================================================================

if "openai_key" not in st.session_state:
    st.session_state.openai_key = ""
if "tavily_key" not in st.session_state:
    st.session_state.tavily_key = ""

# ============================================================================
# HERO
# ============================================================================

st.markdown('<div class="page-title">AI Chatbot </div>', unsafe_allow_html=True)
st.markdown('<div class="page-sub">Hands-on modules exploring core LLM application patterns — from basic inference to retrieval-augmented generation and tool use.</div>', unsafe_allow_html=True)

# Info banner
openai_set = bool(st.session_state.openai_key)
tavily_set = bool(st.session_state.tavily_key)
if not openai_set:
    st.markdown('<div class="info-banner">Enter your API keys below to get started.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="info-banner">API keys saved — select a module below to begin.</div>', unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ============================================================================
# API KEYS
# ============================================================================

st.markdown('<div class="api-label">API Keys</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown('[How to get your OpenAI API key](https://academy.datasciencedojo.com/pages/how-to-create-your-own-openai-api-key)', unsafe_allow_html=True)
    openai_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-proj-...",
        value=st.session_state.openai_key,
    )
with col2:
    st.markdown('[How to get your Tavily API key](https://academy.datasciencedojo.com/pages/how-to-create-your-own-tavily-api-key)', unsafe_allow_html=True)
    tavily_input = st.text_input(
        "Tavily API Key",
        type="password",
        placeholder="tvly-...",
        value=st.session_state.tavily_key,
    )

with st.container():
    st.markdown('<div class="save-btn">', unsafe_allow_html=True)
    if st.button("Save API Keys"):
        errors = []
        if openai_input and not openai_input.startswith("sk-"):
            errors.append("Invalid OpenAI key format.")
        if tavily_input and not tavily_input.startswith("tvly-"):
            errors.append("Invalid Tavily key format.")
        if errors:
            st.error(" ".join(errors))
        else:
            st.session_state.openai_key = openai_input
            st.session_state.tavily_key = tavily_input
            st.success("Keys saved.")
    st.markdown('</div>', unsafe_allow_html=True)

k1, k2 = st.columns(2)
with k1:
    if st.session_state.openai_key:
        st.success("OpenAI connected")
    else:
        st.warning("OpenAI not set")
with k2:
    if st.session_state.tavily_key:
        st.success("Tavily connected")
    else:
        st.warning("Tavily not set — needed for Search Chat")

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ============================================================================
# MODULE GRID
# ============================================================================

st.markdown('<div class="sec-label">Modules</div>', unsafe_allow_html=True)

modules = [
    {
        "num": "01",
        "title": "Basic AI Chat",
        "desc": "Direct conversational interface with a language model. No tools, no retrieval — just the base model.",
        "page": "pages/1_Basic_Chatbot.py"
    },
    {
        "num": "02",
        "title": "Search-Enabled Chat",
        "desc": "Extends base chat with live web search via Tavily, enabling access to current information from the web",
        "page": "pages/2_Chatbot_Agent.py"
    },
    {
        "num": "03",
        "title": "RAG — Retrieval-Augmented Generation",
        "desc": "Upload documents and query them using semantic search. Grounds model responses in your own sources.",
        "page": "pages/3_RAG.py"
    },
    {
        "num": "04",
        "title": "MCP Agent",
        "desc": "Tool-use via the Model Context Protocol. Connects the model to structured external services and APIs.",
        "page": "pages/4_MCP_Agent.py"
    },
    {
        "num": "05",
        "title": "Deep Agent Skill Architecture",
        "desc": "A deepagents harness with planning, a workspace filesystem, and progressively-disclosed Skills — Excel, Word, PDF, and data analysis.",
        "page": "pages/5_Deep_Agent_Skill_Architecture.py"
    },
]

# Render in 2-column pairs
for i in range(0, len(modules), 2):
    col1, col2 = st.columns(2)
    for col, m in zip([col1, col2], modules[i:i+2]):
        with col:
            with st.container(border=True):
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:8px; margin-bottom:0.5rem;">
                    <span class="module-number">{m['num']}</span>
                    <span class="module-title">{m['title']}</span>
                </div>
                <div class="module-desc" style="margin-bottom:0.85rem;">{m['desc']}</div>
                """, unsafe_allow_html=True)
                if st.button("Open module", key=m["page"]):
                    st.switch_page(m["page"])

# ============================================================================
# FOOTER
# ============================================================================

st.markdown('<div class="footer-note">LLM Bootcamp · Session Project</div>', unsafe_allow_html=True)