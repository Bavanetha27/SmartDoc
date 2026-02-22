import streamlit as st

st.set_page_config(
    page_title="SmartDoc",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session states
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None


# Landing Content
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
h1 {
    text-align: center;
    color: #38bdf8;
}
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 200px;
}
.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>🚀 DocuMind AI</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="center">
    <h3>Smart Document Question Answering System</h3>
    <p>Upload large PDFs and get intelligent answers instantly.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Get Started"):
        st.switch_page("pages/2_Login.py")