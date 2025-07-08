# 📈 Real-time Stock Price Anomaly Detector

A Python application that monitors real-time stock prices and raises alerts when unusual patterns or anomalies are detected using statistical and AI/ML techniques.

---

## 🚀 Features

- 📊 Real-time stock price tracking using public APIs (e.g., `yfinance`)
- 🧠 Anomaly detection using:
  - Rule-based thresholds
  - Optional LSTM-based model
- ✅ Handles missing/invalid data gracefully
- 🔔 Sends alerts via email (optional Slack integration)
- 🔧 Easily configurable stock list, thresholds, and polling intervals
- 🧩 Modular, extensible, and production-ready structure

---

## 🛠️ Tech Stack

- **Python 3.8+**
- [`yfinance`](https://pypi.org/project/yfinance/)
- `pandas`, `numpy`, `scikit-learn`
- `matplotlib` (for visualizations)
- `torch` (optional, for LSTM model)
- `smtplib` (for email alerting)

---

## 🧪 Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/stock-anomaly-detector.git
   cd stock-anomaly-detector
2. **Create and activate a virtual environment (recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install required dependencies**:

   ```bash
   pip install -r requirements.txt

---

## ⚙️ Configuration

Edit config/settings.py before running the application.  
**🔍 Stock Monitoring**
```bash
WATCHED_STOCKS = ["AAPL", "GOOGL", "MSFT", "TSLA"]
Replace with your desired stock symbols.
```

**⏱️ Fetch Interval**
```bash
FETCH_INTERVAL = 60  # In seconds
Adjust how often the app fetches new prices.
```

**🚨 Anomaly Detection Rules**
```bash
ANOMALY_RULES = {
    "price_spike_percent": 5.0,
    "moving_avg_window": 5
}
Modify to change the anomaly sensitivity.
```
**✉️ Email Alerts**
Update credentials and recipients:

```bash
EMAIL_SETTINGS = {
    "sender": "your_email@example.com",
    "recipients": ["recipient@example.com"],
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "username": "your_email@example.com",
    "password": "your_password"
}
```
ℹ️ Ensure your email service supports SMTP and app-specific passwords if required.

**💬 Slack Alerts (Optional)**  
To enable Slack alerts:
- Create an Incoming Webhook.
- Update the settings:
    ```bash
    SLACK_SETTINGS = {
        "webhook_url": "https://hooks.slack.com/services/your/slack/webhook"
    }

    ALERT_METHODS = {
        "email": True,
        "slack": True
    }
    ```