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
