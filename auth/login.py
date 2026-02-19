import streamlit as st
from auth.auth_utils import authenticate_user

def login_page():
    st.title("Sign In")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        # ---- DEFAULT ADMIN (PROTOTYPE FALLBACK) ----
        if username == "admin" and password == "admin123":
            st.session_state.user_id = 0
            st.session_state.role = "admin"
            st.session_state.page = "dashboard"
            return

        # ---- DEMO USER (PRESENTATION MODE) ----
        if username == "demo" and password == "demo123":
            st.session_state.user_id = -1
            st.session_state.role = "demo"
            st.session_state.page = "dashboard"
            return

        # ---- NORMAL AUTH FLOW ----
        user = authenticate_user(username, password)
        if user:
            st.session_state.user_id = user["id"]
            st.session_state.role = user["role"]
            st.session_state.page = "dashboard"
        else:
            st.error("Invalid username or password")

    if st.button("Home"):
        st.session_state.page = "home"
