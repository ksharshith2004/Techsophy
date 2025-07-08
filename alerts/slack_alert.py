# alerts/slack_alert.py

import requests
from config.settings import SLACK_WEBHOOK_URL

def send_slack_alert(message: str):
    """
    Send an alert message to a Slack channel using an incoming webhook.

    Args:
        message (str): The message content to send.
    """
    payload = {"text": message}

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print("✅ Slack alert sent successfully.")
        else:
            print(f"❌ Slack alert failed with status code {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Exception occurred while sending Slack alert: {e}")
