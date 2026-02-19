def register_page():
    import streamlit as st
    from database.db import get_connection

    st.title("Register")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        conn = get_connection()
        cursor = conn.cursor()

        # Make username check case-insensitive
        cursor.execute("SELECT * FROM users WHERE LOWER(username)=?", (username.lower(),))
        if cursor.fetchone():
            st.error("Username already exists! Try another.")
        else:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            conn.commit()
            st.success("Registration successful! Please log in.")
        conn.close()
