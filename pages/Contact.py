import streamlit as st

st.header("Contact me")

with st.form(key="email_form"):
    email = st.text_input("E-mail address")
    msg = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print('a')
