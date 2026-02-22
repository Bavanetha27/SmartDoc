import streamlit as st
from utils import create_rag_pipeline, ask_question

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please login first.")
    st.switch_page("pages/2_Login.py")

st.title("🤖 AI Document Assistant")

st.sidebar.title("📊 Processing Log")

if "logs" not in st.session_state:
    st.session_state.logs = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

log_placeholder = st.sidebar.empty()

def add_log(message):
    st.session_state.logs.append(message)
    log_placeholder.markdown("\n".join(st.session_state.logs))

# Always render logs (important)
log_placeholder.markdown("\n".join(st.session_state.logs))

# Logout button
if st.sidebar.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.vectorstore = None
    st.session_state.logs = []
    st.switch_page("app.py")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    # Reset logs when new file uploaded
    if st.session_state.vectorstore is None:
        st.session_state.logs = []

        with st.spinner("Processing document..."):
            st.session_state.vectorstore = create_rag_pipeline(
                uploaded_file,
                log_func=add_log
            )

        st.success("✅ Document Indexed Successfully!")

    st.divider()
    st.subheader("💬 Ask Questions")

    question = st.text_input("Ask your question")

    if question:
        if st.session_state.vectorstore is None:
            st.error("Please upload and process a document first.")
        else:
            with st.spinner("Generating answer..."):
                answer = ask_question(st.session_state.vectorstore, question)

            st.subheader("Answer:")
            st.write(answer)