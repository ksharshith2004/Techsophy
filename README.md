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
