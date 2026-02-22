import streamlit as st
import bcrypt
from db import users_collection

st.set_page_config(
    page_title="SmartDoc",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
/* Hide Streamlit default sidebar */
section[data-testid="stSidebar"] {
    display: none !important;
}

/* Remove sidebar collapse button */
button[kind="header"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🔐 Login")


email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = users_collection.find_one({"email": email})

    if user and bcrypt.checkpw(password.encode(), user["password"]):
        st.session_state.authenticated = True
        st.session_state.user = user["username"]
        st.success("Login Successful!")
        st.switch_page("pages/3_AI_Chat.py")
    else:
        st.error("Invalid Email or Password")

st.markdown("Don't have an account?")
if st.button("Register Here"):
    st.switch_page("pages/1_Register.py")