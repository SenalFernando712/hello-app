import streamlit as st

# Centered title using Markdown syntax
st.markdown("<h1 style='text-align: center;'>Welcome to BCI Choir Finance App </h1>", unsafe_allow_html=True)

# Create two columns layout
col1, col2 = st.columns(2)

# Username input field
with col1:
    username = st.text_input("Username")

# Password input field
with col2:
    password = st.text_input("Password", type="password")



