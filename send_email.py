import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = 'cipriangheorghecapata@gmail.com'
password = 'ukqyvxgzcdhafvia'

receiver = 'cipriangheorghecapata@gmail.com'
context = ssl.create_default_context()

msg = """\
Subject: <subject>
Hi
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, msg)