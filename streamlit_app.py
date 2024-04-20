import streamlit as st

login_details = {
  "credentials": {
    "usernames": {
      "jsmith": {
        "email": "abc@yahoo.com",
        "name": "John Smith",
        "password": 123
      },
      "rbriggs": {
        "email": "rbriggs@gmail.com",
        "name": "Rebecca Briggs",
        "password": 456
      }
    }
  },
  "cookie": {
    "expiry_days": 1,
    "key": "some_signature_key",
    "name": "cookie_name_streamlit_authenticator"
  },
  "preauthorized": {
    "emails": [
      "abc@gmail.com"
    ]
  }
}
placeholder = st.empty()
placeholder.title("login")

with placeholder.form("login"):
    username = st.text_input("username")
    password = st.text_input("password", type="password")
    submit_button = st.form_submit_button("submit")


    if submit_button:
        if username in login_details["credentials"]["usernames"]:
            print(f"username: {username} found")
            print(f"password: {login_details['credentials']['usernames'][username]['password']}")
            if password == str(login_details["credentials"]["usernames"][username]["password"]):
                print(password)
                st.success("Login successful")
                placeholder.empty()
                with placeholder.container():
                    st.write(f"hello, {login_details['credentials']['usernames'][username]['name']}")
            else:
                st.error("Login failed")

'''
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
'''
