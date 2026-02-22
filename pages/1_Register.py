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

st.title("📝 Register")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    if users_collection.find_one({"email": email}):
        st.error("User already exists!")
    else:
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_pw
        })

        st.success("Registration Successful!")
        st.switch_page("pages/2_Login.py")