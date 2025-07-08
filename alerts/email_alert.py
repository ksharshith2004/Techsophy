# alerts/email_alert.py

import smtplib
from email.mime.text import MIMEText
from config.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_RECEIVERS

def send_email_alert(subject: str, message: str):
    """
    Send an email alert with the given subject and message.

    Args:
        subject (str): Email subject
        message (str): Email body content
    """
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_HOST_USER
        msg["To"] = ", ".join(EMAIL_RECEIVERS)

        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, EMAIL_RECEIVERS, msg.as_string())
        print("✅ Email alert sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email alert: {e}")
