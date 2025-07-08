# models/rule_based.py

import numpy as np

class RuleBasedAnomalyDetector:
    def __init__(self, window_size=5, threshold=0.05):
        """
        Parameters:
        - window_size: Number of previous data points to consider for moving average
        - threshold: Percentage deviation from the moving average to be flagged as anomaly
        """
        self.window_size = window_size
        self.threshold = threshold

    def detect(self, price_series):
        """
        Detect anomalies in a list of stock prices.

        Parameters:
        - price_series: List of floats, where each float is a stock price

        Returns:
        - List of tuples (index, price, reason) for each anomaly
        """
        anomalies = []

        if len(price_series) <= self.window_size:
            return anomalies  # Not enough data to evaluate

        for i in range(self.window_size, len(price_series)):
            window = price_series[i - self.window_size:i]
            current_price = price_series[i]
            moving_avg = np.mean(window)

            if moving_avg == 0:
                continue  # Prevent divide-by-zero

            deviation = abs(current_price - moving_avg) / moving_avg

            if deviation > self.threshold:
                reason = f"{current_price:.2f} deviates {deviation*100:.2f}% from avg {moving_avg:.2f}"
                anomalies.append((i, current_price, reason))

        return anomalies
