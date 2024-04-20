import streamlit as st

# Centered title using Markdown syntax
st.markdown("<h1 style='text-align: center;'>Welcome to BCI Choir Finance App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left;'>Enter Your Credentials</h3>", unsafe_allow_html=True)
# Username input field
username = st.text_input("Username")

# Password input field
password = st.text_input("Password", type="password")

# Sign-in button
if st.button("Sign In"):
    # Your sign-in logic goes here
    st.write("Signing in...")
    if (username == 'Senal') && (password == 'S3N4L') :
        st.write('Done')
    



