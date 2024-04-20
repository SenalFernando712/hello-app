import streamlit as st

# Centered title using Markdown syntax
st.markdown("<h1 style='text-align: center;'>Enter Your Credentials</h1>", unsafe_allow_html=True)

# Username input field
username = st.text_input("Username")

# Password input field
password = st.text_input("Password", type="password")



