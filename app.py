import streamlit as st

st.set_page_config(
    page_title="SmartDoc",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None


# ---------------------- DARK SAAS CSS ---------------------- #
st.markdown("""
<style>

/* Global Dark Theme */
html, body, [class*="css"] {
    background-color: #0b0f19;
    color: #e5e7eb;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 60px;
}

.logo {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* Hero */
.hero {
    text-align: center;
    padding: 140px 20px 80px 20px;
}

.hero-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(90deg,#60a5fa,#a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    font-size: 20px;
    color: #9ca3af;
    margin-top: 25px;
    margin-bottom: 45px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border-radius: 10px;
    padding: 14px 28px;
    font-weight: 600;
    font-size: 16px;
    border: none;
    transition: all 0.25s ease;
    box-shadow: 0 0 20px rgba(139,92,246,0.4);
}

.stButton>button:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 35px rgba(139,92,246,0.7);
}

/* Feature Section */
.section {
    padding: 100px 60px;
}

.feature-card {
    background: #111827;
    padding: 35px;
    border-radius: 16px;
    transition: 0.3s ease;
    border: 1px solid #1f2937;
}

.feature-card:hover {
    transform: translateY(-6px);
    border: 1px solid #6366f1;
    box-shadow: 0 0 25px rgba(99,102,241,0.3);
}

/* CTA */
.cta-box {
    margin: 100px 60px;
    padding: 80px;
    text-align: center;
    background: #111827;
    border-radius: 20px;
    border: 1px solid #1f2937;
}

/* Footer */
.footer {
    text-align: center;
    padding: 50px;
    color: #6b7280;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------- NAVBAR ---------------------- #

col1, col2 = st.columns([3,1])

with col1:
    st.markdown('<div class="logo">📘 SmartDoc</div>', unsafe_allow_html=True)

with col2:
    login_col, register_col = st.columns(2)
    with login_col:
        if st.button("Login"):
            st.switch_page("pages/2_Login.py")
    with register_col:
        if st.button("Register"):
            st.switch_page("pages/1_Register.py")


# ---------------------- HERO ---------------------- #

st.markdown("""
<div class="hero">
    <div class="hero-title">
        AI-Powered Document Intelligence
    </div>
    <div class="hero-sub">
        Upload your PDFs and turn them into intelligent conversations instantly.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,1,2])

with col2:
    if st.button("Get Started Free 🚀", use_container_width=True):
        st.switch_page("pages/2_Login.py")


# ---------------------- FEATURES ---------------------- #

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Why SmartDoc?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Instant AI Answers</h3>
        <p>Ask natural questions and get contextual responses in seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📂 Large PDF Support</h3>
        <p>Handles hundreds of pages with advanced vector search indexing.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🔐 Private & Secure</h3>
        <p>Your documents are session-isolated and processed securely.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------- CTA ---------------------- #

st.markdown("""
<div class="cta-box">
    <h2>Ready to Transform Your Documents?</h2>
    <p>Start using SmartDoc today and experience AI-powered document understanding.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,1,2])

with col2:
    if st.button("Create Account 🚀", use_container_width=True):
        st.switch_page("pages/1_Register.py")


# ---------------------- FOOTER ---------------------- #

st.markdown("""
<div class="footer">
© 2026 SmartDoc • Built with Streamlit + LangChain + FAISS
</div>
""", unsafe_allow_html=True)