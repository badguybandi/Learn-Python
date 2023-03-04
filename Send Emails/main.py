import smtplib
import ssl
import getpass
from email.message import EmailMessage

subject = "Test Email"
body = "This is a test email"
sender_email = "aaronbandado@gmail.com"
receiver_email = "aaronbandado@gmail.com"
password = getpass.getpass("Enter the password:")

message = EmailMessage()

message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
"""

message.add_alternative(html, subtype='html')

context = ssl.create_default_context()

print("Sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email,message.as_string())
print("Success!")