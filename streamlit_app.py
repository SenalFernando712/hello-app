import streamlit as st

# Centered title using Markdown syntax
st.markdown("<h1 style='text-align: center;'>Welcome to BCI Choir Finance App </h1>", unsafe_allow_html=True)

# Username input field with reduced size and centered
st.write('<style>input[type="text"] { width: 200px; text-align: center; }</style>', unsafe_allow_html=True)
username = st.text_input("Username")

# Password input field with reduced size and centered
st.write('<style>input[type="password"] { width: 200px; text-align: center; }</style>', unsafe_allow_html=True)
password = st.text_input("Password", type="password")


