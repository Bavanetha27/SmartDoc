import streamlit as st
from utils import create_rag_pipeline, ask_question

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Please login first.")
    st.stop()

st.title("🤖 AI Document Assistant")

st.sidebar.title("Navigation")
if st.sidebar.button("Logout"):
    st.session_state.authenticated = False
    st.switch_page("app.py")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    if "vectorstore" not in st.session_state:
        with st.spinner("Processing document..."):
            st.session_state.vectorstore = create_rag_pipeline(uploaded_file)
        st.success("Document Indexed!")

    question = st.text_input("Ask your question")

    if question:
        with st.spinner("Generating answer..."):
            answer = ask_question(st.session_state.vectorstore, question)

        st.subheader("Answer:")
        st.write(answer)