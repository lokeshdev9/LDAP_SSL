import smtplib
from email.mime.text import MIMEText

# Email Configuration
smtp_server = 'your_smtp_server'
smtp_port = 587
smtp_username = 'your_smtp_username'
smtp_password = 'your_smtp_password'
sender_email = 'sender@example.com'
recipient_email = 'recipient@example.com'

def send_email_notification(change_info):
    subject = 'LDAP SSL Certificate Change Notification'
    body = f'The SSL certificate for LDAP server has changed.\n\nChange Details:\n{change_info}'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

# Usage example:
# send_email_notification("Previous Fingerprint: abcdef\nCurrent Fingerprint: 123456")

