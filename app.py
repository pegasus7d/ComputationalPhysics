import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'sabpeacehai@gmail.com'
receiver_email = 'debayanbiswas1111@gmail.com'
subject = 'Subject of the email'
body = 'Body of the email'

# Your Gmail credentials (make sure to enable "Less secure app access" in your Google account settings)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sabpeacehai@gmail.com'
smtp_password = 'ropx pnbw qnvy zfao'

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start TLS for security
    server.starttls()

    # Login to the SMTP server
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Email sent successfully!')
