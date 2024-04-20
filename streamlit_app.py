import streamlit as st

# Create two columns layout
col1, col2 = st.coloums(2)

# Username input field
with col1:
    username = st.text_input("Username")

# Password input field
with col2:
    password = st.text_input("Password", type="password")

st.write('Hello World!')
st.write('Hi There im editing')


