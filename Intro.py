from email.message import EmailMessage
from app2.py import password
import ssl
import smtplib

email_sender = 'timmisettysivaanil143@gmail.com'
email_password = password

email_receiver = 'mosom66741@dogemn.com'

subject = "Don't forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
#ijiujn
#another commment

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)  
    smtp.sendmail(email_sender, email_receiver, em.as_string())


