import streamlit as st
from send_email import send_email
st.header("Contact me")

with st.form(key="email_form"):
    email = st.text_input("E-mail address")
    raw_msg = st.text_area("Your message")
    msg = f"""\
Subject: New email from {email}

From: {email}
{raw_msg}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(msg)
        st.info("Your E-mail has been sent.")