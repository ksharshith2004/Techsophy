# config/settings.py

import os
import logging

# Create logs directory if it doesn't exist
os.makedirs("data/logs", exist_ok=True)

# Logging configuration
LOG_FILE = "data/logs/anomaly.log"
LOG_LEVEL = logging.INFO  # Could be DEBUG, INFO, WARNING, ERROR, CRITICAL

logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# List of stock symbols to monitor
WATCHED_STOCKS = [
    "AAPL",  # Apple
    "GOOGL", # Google
    "MSFT",  # Microsoft
    "TSLA",  # Tesla
]

# Interval (in seconds) between API fetches
FETCH_INTERVAL = 60  # 1 minute

# Anomaly detection settings
ANOMALY_RULES = {
    "price_spike_percent": 5.0,  # Alert if price jumps > 5% from average
    "moving_avg_window": 5       # Window size for moving average
}

# LSTM model settings
USE_LSTM_MODEL = False

# Alert methods
ALERT_METHODS = {
    "email": True,
    "slack": False
}

# Email alert config
EMAIL_SETTINGS = {
    "sender": "your_email@example.com",
    "recipients": ["recipient@example.com"],
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "username": "your_email@example.com",
    "password": "your_password"
}

# Slack alert config
SLACK_SETTINGS = {
    "webhook_url": "https://hooks.slack.com/services/your/slack/webhook"
}
