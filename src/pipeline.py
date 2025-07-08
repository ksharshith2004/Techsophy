# src/pipeline.py

import time
import yfinance as yf
from config.settings import (
    WATCHED_STOCKS, FETCH_INTERVAL, ALERT_METHODS,
    ANOMALY_RULES, USE_LSTM_MODEL
)

from src.validator import validate_data
from models.rule_based import detect_anomalies as rule_based_detect
from models.lstm_model import detect_anomalies as lstm_detect

from alerts.email_alert import send_email_alert
from alerts.slack_alert import send_slack_alert


def fetch_stock_data(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1d", interval="1m")
        if not data.empty:
            return data['Close'].tolist()
        return []
    except Exception as e:
        print(f"[ERROR] Failed to fetch data for {ticker}: {e}")
        return []


def main():
    print("[INFO] Starting Stock Anomaly Detector...")
    while True:
        for ticker in WATCHED_STOCKS:
            print(f"[INFO] Checking {ticker}...")
            price_series = fetch_stock_data(ticker)

            if not validate_data(price_series):
                print(f"[WARN] Invalid data for {ticker}, skipping.")
                continue

            if USE_LSTM_MODEL:
                anomalies = lstm_detect(ticker, price_series)
            else:
                anomalies = rule_based_detect(ticker, price_series, ANOMALY_RULES)

            if anomalies:
                message = f"Anomaly detected for {ticker}: {anomalies}"
                print(f"[ALERT] {message}")
                
                if ALERT_METHODS.get("email"):
                    send_email_alert(ticker, message)

                if ALERT_METHODS.get("slack"):
                    send_slack_alert(ticker, message)

        print(f"[INFO] Sleeping for {FETCH_INTERVAL} seconds...\n")
        time.sleep(FETCH_INTERVAL)


if __name__ == "__main__":
    main()
