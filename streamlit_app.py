import streamlit as st

# Centered title using Markdown syntax
st.markdown("<h1 style='text-align: center;'>Welcome to BCI Choir Finance App</h1>", unsafe_allow_html=True)

# Flag to track login status
logged_in = False

# If not logged in, show login page
if not logged_in:
    # Title for credentials
    st.markdown("<h3 style='text-align: left;'>Enter Your Credentials</h3>", unsafe_allow_html=True)

    # Username input field
    username = st.text_input("Username")

    # Password input field
    password = st.text_input("Password", type="password")

    # Sign-in button
    if st.button("Sign In"):
        # Your sign-in logic goes here
        if (username == 'Senal') and (password == 'S3N4L'):
            logged_in = True

# If logged in, show "Hi" page
if logged_in:
    # Clear the page
    st.empty()
    # Show the "Hi" title
    st.markdown("<h1 style='text-align: center;'>Hi</h1>", unsafe_allow_html=True)
