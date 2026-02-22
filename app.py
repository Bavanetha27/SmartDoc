import streamlit as st
from utils import create_rag_pipeline

st.set_page_config(
    page_title="Large Document QA System",
    layout="wide"
)

st.title("📘 Large Document Question Answering System")
st.markdown("Upload a large PDF and ask questions from it.")

# File uploader
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    st.success("Document uploaded successfully!")

    # Create RAG pipeline once
    if "qa_chain" not in st.session_state:
        with st.spinner("Processing document... Please wait."):
            try:
                st.session_state.qa_chain = create_rag_pipeline(uploaded_file)
                st.success("Document indexed successfully!")
            except Exception as e:
                st.error(f"Error: {e}")

    # Question input
    question = st.text_input("Ask your question")

    if question:
        with st.spinner("Generating answer..."):
            try:
                response = st.session_state.qa_chain.run(question)

                st.subheader("Answer:")
                st.write(response)

            except Exception as e:
                st.error(f"Error generating answer: {e}")