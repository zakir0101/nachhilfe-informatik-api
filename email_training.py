# Import smtplib for the actual sending function
import smtplib
from flask_mail import Mail, Message
import os

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
# Create a text/plain message

msg = EmailMessage()
msg.set_content("this is content of the message")

# me == the sender's email address
# you == the recipient's email address

msg['Subject'] = f'subject of the email'
msg['From'] = "zakir.elkheir@gmail.com"
msg['To'] = "zakir1996@gmail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost', 5000)
s.send_message(msg)
s.quit()
