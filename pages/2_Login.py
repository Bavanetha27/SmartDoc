import streamlit as st

st.title("🔐 Login to Continue")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.session_state.authenticated = True
        st.success("Login Successful!")
        st.switch_page("pages/3_AI_Chat.py")
    else:
        st.error("Invalid Credentials")

st.markdown("Demo Login → admin / 1234")