import streamlit as st

st.set_page_config(
    page_title="Crestline Internal Assistant",
    layout="wide",
    page_icon="🤖"
)

st.markdown(
    "<style>"
    "body { background-color: #EFF4FF; }"
    ".stApp { background: linear-gradient(180deg, #F4F8FF 0%, #EBF2FF 100%); }"
    ".hero-card { background: #FFFFFF; padding: 32px 32px 28px; border-radius: 24px; border: 1px solid #D9E6FF; box-shadow: 0 20px 45px rgba(15, 64, 133, 0.08); margin-bottom: 24px; }"
    ".hero-title { color: #0E3A8A; font-size: 3rem; font-weight: 800; margin-bottom: 12px; line-height: 1.05; }"
    ".hero-subtitle { color: #1E40AF; font-size: 1.05rem; margin-bottom: 24px; }"
    ".hero-pill { display: inline-flex; align-items: center; gap: 8px; background: rgba(14, 56, 138, 0.08); color: #0E3A8A; border-radius: 999px; padding: 10px 16px; font-size: 0.95rem; margin-bottom: 18px; }"
    ".hero-list { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin-top: 0.8rem; }"
    ".hero-list-item { background: rgba(14, 56, 138, 0.05); padding: 14px 16px; border-radius: 14px; border: 1px solid rgba(14, 56, 138, 0.12); color: #0B3D91; font-weight: 500; }"
    ".info-box { background: rgba(11, 61, 145, 0.08); padding: 18px 20px; border-radius: 18px; border: 1px solid rgba(11, 61, 145, 0.16); color: #0F4DB5; margin-bottom: 28px; font-size: 1rem; }"
    ".section-title { color: #0F52B5; font-size: 1.25rem; font-weight: 700; margin: 18px 0 12px; }"
    ".chat-user { background: #D8E9FF; padding: 18px; border-radius: 18px; margin-bottom: 14px; border: 1px solid #B8D0FF; }"
    ".chat-assistant { background: #FFFFFF; padding: 18px; border-radius: 18px; margin-bottom: 18px; border: 1px solid #DFE9FB; }"
    ".sidebar-box { background: rgba(11, 61, 145, 0.06); padding: 22px; border-radius: 20px; border: 1px solid rgba(11, 61, 145, 0.16); }"
    ".sidebar-description { color: #1D4ED8; font-size: 1rem; margin-bottom: 18px; }"
    ".example-card { background: #FFFFFF; padding: 16px 18px; border-radius: 16px; margin-bottom: 12px; border: 1px solid #D4E2FF; color: #0B3D91; box-shadow: 0 10px 24px rgba(11, 61, 145, 0.06); }"
    ".stTextInput>div>div>input { border-radius: 14px; padding: 18px 16px; font-size: 1rem; }"
    ".stButton>button { background-color: #0B3D91; color: white; border-radius: 12px; padding: 0.85rem 1.3rem; font-weight: 600; }"
    ".stButton>button:hover { background-color: #08397A; }"
    "</style>"
    ,
    unsafe_allow_html=True,
)

st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
st.markdown("<div class='hero-pill'>🤖 Crestline Internal Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-title'>Your enterprise-ready AI guide for Crestline Technologies</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Ask questions about sales performance, HR policies, marketing campaigns, technical documentation, and operational best practices.</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='hero-list'>"
    "<div class='hero-list-item'>💰 Sales, metrics, and KPIs</div>"
    "<div class='hero-list-item'>👥 HR policies and PTO</div>"
    "<div class='hero-list-item'>📣 Marketing campaigns and strategy</div>"
    "<div class='hero-list-item'>🛠️ Product documentation and API</div>"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='info-box'>Professional demo interface. Connect this assistant to Crestline systems for live responses from HR, sales, marketing, and product documentation.</div>", unsafe_allow_html=True)

col1, col2 = st.columns([2.7, 1.1])
with col1:
    st.markdown("<div class='section-title'>Live conversation</div>", unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input(
        "Enter your question:",
        "What are the primary KPIs for this quarter?",
    )

    def get_demo_response(query: str) -> str:
        text = query.strip().lower()

        if "pto" in text or "time off" in text or "request pto" in text:
            return (
                "To request PTO, please submit a time-off request through the Crestline HR portal, "
                "select your dates, and await manager approval. If you need help, contact HR at hr@crestline.tech."
            )

        if "kpi" in text or "top kpis" in text or "key performance indicators" in text:
            return (
                "The current focus KPIs include quarterly revenue growth, customer retention rate, "
                "and sales pipeline velocity. For detailed metrics, review the sales dashboard in the Analytics workspace."
            )

        if "sold" in text and "crestline x" in text:
            return (
                "I don’t have exact unit counts in this demo interface, but Crestline X sales are tracked in the sales ledger and retail analytics dashboard. "
                "For the most recent figures, please consult the Crestline Sales dashboard or contact the sales ops team for the latest report."
            )

        if "marketing" in text and "campaign" in text:
            return (
                "This month, the marketing team is executing a product launch campaign and a customer engagement push. "
                "Check the internal marketing schedule for channel-specific details."
            )

        if "api documentation" in text or "customer portal" in text:
            return (
                "You can find the customer portal API documentation in the Crestline Confluence site under Product Resources, "
                "or by visiting the developer docs section in the internal docs portal."
            )

        return (
            "This is a refined demo experience for the internal assistant. "
            "Connect backend services here to return real answers from Crestline analytics, policies, or documentation."
        )

    if st.button("Submit") and user_input:
        response = get_demo_response(user_input)
        st.session_state.history.append((user_input, response))

    if st.session_state.history:
        for prompt, answer in reversed(st.session_state.history):
            st.markdown(f"<div class='chat-user'><strong>User</strong><br>{prompt}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-assistant'><strong>Assistant</strong><br>{answer}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='sidebar-box'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Example questions</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-description'>Use these templates to quickly ask the assistant for help across Crestline.</div>", unsafe_allow_html=True)
    st.markdown("<div class='example-card'>What are the top KPIs for this quarter?</div>", unsafe_allow_html=True)
    st.markdown("<div class='example-card'>How do I request PTO?</div>", unsafe_allow_html=True)
    st.markdown("<div class='example-card'>What marketing campaigns are planned next month?</div>", unsafe_allow_html=True)
    st.markdown("<div class='example-card'>Where can I find the API documentation for the customer portal?</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='info-box'>Designed for Crestline internal collaboration and operational support.</div>", unsafe_allow_html=True)
st.markdown("<div class='footer-text'>This assistant is a premium internal solution for Crestline teams seeking fast, reliable answers on operations and documentation.</div>", unsafe_allow_html=True)
