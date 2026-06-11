"""
Chatbot Agent - AI agent with live web search via Tavily.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import streamlit as st
import html
import re
import os

from utils.styles import apply_base_css
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent

_MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")


def _render_assistant_text(text: str) -> None:
    text = text or ""
    parts: list[str] = []
    last = 0
    for m in _MD_LINK.finditer(text):
        parts.append(html.escape(text[last : m.start()]))
        label, raw_url = m.group(1), m.group(2).strip()
        if raw_url.startswith(("http://", "https://")):
            href = html.escape(raw_url, quote=True)
            parts.append(
                f'<a href="{href}" target="_blank" rel="noopener noreferrer">'
                f"{html.escape(label)}</a>"
            )
        else:
            parts.append(html.escape(m.group(0)))
        last = m.end()
    parts.append(html.escape(text[last:]))
    st.markdown(
        f'<div style="white-space: pre-wrap;">{"".join(parts)}</div>',
        unsafe_allow_html=True,
    )


# =============================================================================
# PAGE SETUP
# =============================================================================

st.set_page_config(
    page_title="Chatbot Agent",
    page_icon=None,
    layout="centered"
)

apply_base_css()

st.markdown('<div class="page-title">Search-Enabled Chat</div>', unsafe_allow_html=True)
st.markdown('<div class="page-caption">AI agent with live web search capabilities via Tavily.</div>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)


# =============================================================================
# SESSION STATE
# =============================================================================

if "agent" not in st.session_state:
    st.session_state.agent = None

if "agent_messages" not in st.session_state:
    st.session_state.agent_messages = []


# =============================================================================
# CHECK API KEYS FROM HOME PAGE
# =============================================================================

openai_key = st.session_state.get("openai_key", "")
tavily_key = st.session_state.get("tavily_key", "")

missing = []
if not openai_key:
    missing.append("OpenAI")
if not tavily_key:
    missing.append("Tavily")

if missing:
    st.markdown(f"""
    <div class="warn-banner">
        Missing API keys: <strong>{", ".join(missing)}</strong>.
        Please go back to the Home page and save your keys first.
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Home"):
        st.switch_page("Home.py")
    st.stop()
else:
    st.markdown("""
    <div class="info-banner">OpenAI and Tavily keys loaded — ready to search and chat.</div>
    """, unsafe_allow_html=True)


# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("**Search-Enabled Chat**")
    st.caption("AI agent with live web search via Tavily.")
    st.divider()
    if st.button("Clear chat"):
        st.session_state.agent_messages = []
        st.session_state.agent = None
        st.rerun()
    if st.button("Home"):
        st.switch_page("Home.py")


# =============================================================================
# CREATE AGENT
# =============================================================================

if not st.session_state.agent:
    os.environ["OPENAI_API_KEY"] = openai_key
    os.environ["TAVILY_API_KEY"] = tavily_key

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    search_tool = TavilySearch(
        max_results=5,
        description=(
            "Search the live web for up-to-date information, "
            "latest figures, prices, releases, sports scores, or anything that may have "
            "changed after the model's knowledge cutoff. Input should always be a search query string."
        ),
    )

    st.session_state.agent = create_agent(llm, tools=[search_tool])


# =============================================================================
# GREETING
# =============================================================================

if not st.session_state.agent_messages:
    greeting = "Hi! My name is Assistant. I can search the web for up-to-date information. What would you like to know today?"
    st.session_state.agent_messages.append({"role": "assistant", "content": greeting})

# =============================================================================
# CHAT HISTORY
# =============================================================================

for message in st.session_state.agent_messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            _render_assistant_text(message["content"])
        else:
            st.write(message["content"])


# =============================================================================
# USER INPUT
# =============================================================================

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.agent_messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching and thinking..."):
            response = st.session_state.agent.invoke({
                "messages": st.session_state.agent_messages
            })
            response_text = response["messages"][-1].content
            _render_assistant_text(response_text)
            st.session_state.agent_messages.append({
                "role": "assistant",
                "content": response_text
            })

