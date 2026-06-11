"""
Shared CSS styles for the LLM Bootcamp Project.
Call the appropriate apply_*_css() function once at the top of each page,
right after st.set_page_config().
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Shared base — used by pages 1-4 (Basic Chatbot, Chatbot Agent, RAG, MCP)
# ---------------------------------------------------------------------------

_BASE_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu, footer { visibility: hidden; }
    /* keep the header transparent so the sidebar collapse arrow stays reachable */
    [data-testid="stHeader"] { background: transparent !important; box-shadow: none !important; }
    [data-testid="stAppDeployButton"] { display: none !important; }
    .stApp { background-color: #ffffff; }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        max-width: 860px !important;
    }
    .page-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #111111;
        margin-bottom: 0.2rem;
        letter-spacing: -0.02em;
    }
    .page-caption {
        font-size: 0.85rem;
        color: #6b7280;
        margin-bottom: 1.25rem;
    }
    .divider {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 0 0 1.25rem;
    }
    .info-banner {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        padding: 0.65rem 1rem;
        font-size: 0.82rem;
        color: #1d4ed8;
        margin-bottom: 1.25rem;
    }
    .warn-banner {
        background: #fffbeb;
        border: 1px solid #fcd34d;
        border-radius: 8px;
        padding: 0.65rem 1rem;
        font-size: 0.82rem;
        color: #92400e;
        margin-bottom: 1.25rem;
    }
</style>
"""

# ---------------------------------------------------------------------------
# Home page — extends base with module grid, API section, and button overrides
# ---------------------------------------------------------------------------

_HOME_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    #MainMenu, footer { visibility: hidden; }
    /* keep the header transparent so the sidebar collapse arrow stays reachable */
    [data-testid="stHeader"] { background: transparent !important; box-shadow: none !important; }
    [data-testid="stAppDeployButton"] { display: none !important; }
    /* keep the sidebar expand control reachable even with the header hidden */
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="collapsedControl"] { visibility: visible !important; }

    .stApp { background-color: #ffffff; }

    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 860px !important;
    }

    .page-title {
        font-size: 1.6rem;
        font-weight: 600;
        color: #111111;
        margin-bottom: 0.35rem;
        letter-spacing: -0.02em;
        text-align: center;
    }
    .page-sub {
        font-size: 0.9rem;
        color: #555555;
        max-width: 500px;
        margin: 0 auto 1.5rem;
        line-height: 1.6;
        text-align: center;
    }

    .info-banner {
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        font-size: 0.82rem;
        color: #1d4ed8;
        margin-bottom: 1.75rem;
        text-align: center;
    }

    .divider {
        border: none;
        border-top: 1px solid #e5e7eb;
        margin: 0 0 1.5rem;
    }

    .sec-label {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 1rem;
    }

    /* 2-column grid */
    .module-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    .module-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1.25rem;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .module-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        background: #f3f4f6;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 600;
        color: #6b7280;
    }

    .module-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: #111111;
        margin: 0;
    }

    .module-desc {
        font-size: 0.8rem;
        color: #6b7280;
        line-height: 1.55;
        flex: 1;
    }

    .module-footer {
        border-top: 1px solid #f3f4f6;
        padding-top: 0.75rem;
        margin-top: 0.25rem;
    }

    /* API section */
    .api-label {
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 0.75rem;
    }

    /* Override Streamlit button inside cards */
    .stButton > button {
        background: #eff6ff !important;
        color: #1d4ed8 !important;
        border: 1px solid #bfdbfe !important;
        border-radius: 6px !important;
        font-size: 0.78rem !important;
        font-weight: 500 !important;
        padding: 0.3rem 0.9rem !important;
        margin: 0 !important;
        width: auto !important;
    }
    .stButton > button:hover {
        background: #dbeafe !important;
        border-color: #93c5fd !important;
    }

    /* Save keys button override */
    .save-btn > button {
        background: #111111 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        padding: 0.45rem 1.2rem !important;
        width: 100% !important;
        margin-top: 0.25rem !important;
    }
    .save-btn > button:hover {
        background: #333333 !important;
    }

    .footer-note {
        text-align: center;
        font-size: 0.7rem;
        color: #d1d5db;
        padding-top: 0.75rem;
        border-top: 1px solid #f3f4f6;
        margin-top: 0.5rem;
    }
</style>
"""

# ---------------------------------------------------------------------------
# Deep Agent page — wider layout with panel, badge, and todo-row styles
# ---------------------------------------------------------------------------

_DEEP_AGENT_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu, footer { visibility: hidden; }
    /* keep the header transparent so the sidebar collapse arrow stays reachable */
    [data-testid="stHeader"] { background: transparent !important; box-shadow: none !important; }
    [data-testid="stAppDeployButton"] { display: none !important; }
    /* keep the sidebar expand control reachable even with the header hidden */
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="collapsedControl"] { visibility: visible !important; }
    .stApp { background: #fbfbfd; }
    /* wider than default so the chat + side panel fit comfortably */
    .block-container {
        padding-top: 1.6rem !important;
        padding-bottom: 7rem !important;
        max-width: 1150px !important;
    }
    /* Header */
    .da-title {
        font-size: 1.45rem; font-weight: 700; color: #0b0b0f;
        letter-spacing: -0.02em; margin-bottom: 0.1rem;
    }
    .da-sub { font-size: 0.86rem; color: #6b7280; margin-bottom: 0.9rem; }
    .da-status {
        display:inline-flex; align-items:center; gap:0.45rem;
        background:#f0fdf4; border:1px solid #bbf7d0; color:#166534;
        border-radius:999px; padding:0.2rem 0.7rem; font-size:0.74rem; font-weight:500;
    }
    .da-dot { width:7px; height:7px; border-radius:50%; background:#22c55e; }
    /* Panel */
    .panel-label {
        font-size:0.68rem; font-weight:700; letter-spacing:0.09em; text-transform:uppercase;
        color:#9aa1ad; margin:0 0 0.6rem 0; display:flex; align-items:center;
        justify-content:space-between;
    }
    .panel-label span {
        background:#eef0f4; color:#6b7280; border-radius:999px;
        padding:0.02rem 0.5rem; font-size:0.66rem;
    }
    .file-meta { color:#9aa1ad; font-size:0.72rem; }
    .badge-new {
        background:#dcfce7; color:#166534; font-size:0.6rem; font-weight:700;
        padding:0.08rem 0.42rem; border-radius:6px; margin-left:0.45rem;
        letter-spacing:0.03em;
    }
    .todo-row { font-size:0.82rem; color:#374151; padding:0.18rem 0; line-height:1.5; }
    .todo-row.done { color:#9aa1ad; text-decoration:line-through; }
    .dot { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:0.55rem; }
    .d-done { background:#22c55e; } .d-prog { background:#f59e0b; } .d-todo { background:#d1d5db; }
    .empty { color:#9aa1ad; font-size:0.8rem; }
    /* Buttons: subtle + rounded */
    .stButton > button, .stDownloadButton > button {
        border-radius:9px !important; font-size:0.8rem !important; font-weight:500 !important;
        border:1px solid #e5e7eb !important;
    }
    .stPopover > div > button {
        border-radius:9px !important; border:1px solid #e5e7eb !important;
        background:#fff !important; font-size:0.82rem !important; font-weight:500 !important;
        text-align:left !important; color:#111 !important;
    }
    .stPopover > div > button:hover { border-color:#bfdbfe !important; background:#f8fafc !important; }
    div[data-testid="stExpander"] { border-radius:10px !important; }
    .warn-banner {
        background:#fffbeb; border:1px solid #fcd34d; border-radius:8px;
        padding:0.6rem 1rem; font-size:0.82rem; color:#92400e; margin-bottom:1rem;
    }
</style>
"""


def apply_base_css():
    """Apply shared styles for pages 1–4."""
    st.markdown(_BASE_CSS, unsafe_allow_html=True)


def apply_home_css():
    """Apply styles for the Home page."""
    st.markdown(_HOME_CSS, unsafe_allow_html=True)


def apply_deep_agent_css():
    """Apply styles for the Deep Agent Skill Architecture page."""
    st.markdown(_DEEP_AGENT_CSS, unsafe_allow_html=True)
