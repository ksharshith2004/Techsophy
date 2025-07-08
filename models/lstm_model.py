# models/lstm_model.py

import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler


class LSTMAnomalyDetector(nn.Module):
    def __init__(self, input_size=1, hidden_size=50, num_layers=1):
        super(LSTMAnomalyDetector, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out


class LSTMDetectorWrapper:
    def __init__(self, window_size=10, threshold=0.05):
        self.model = LSTMAnomalyDetector()
        self.window_size = window_size
        self.threshold = threshold
        self.scaler = MinMaxScaler()

        # For demo purposes, model is not trained
        self.trained = False

    def detect(self, price_series):
        """
        Takes a price series and returns anomalies based on LSTM predictions.
        """
        if len(price_series) <= self.window_size:
            return []

        # Normalize data
        prices = np.array(price_series).reshape(-1, 1)
        scaled_prices = self.scaler.fit_transform(prices)

        # Create sequences
        X, y = [], []
        for i in range(len(scaled_prices) - self.window_size):
            X.append(scaled_prices[i:i + self.window_size])
            y.append(scaled_prices[i + self.window_size])

        X = torch.tensor(X, dtype=torch.float32)
        y = np.array(y)

        if not self.trained:
            return []  # Skip detection if model is not trained

        self.model.eval()
        with torch.no_grad():
            preds = self.model(X).numpy()

        anomalies = []
        for i in range(len(preds)):
            deviation = abs(preds[i][0] - y[i][0])
            if deviation > self.threshold:
                original_index = i + self.window_size
                original_price = price_series[original_index]
                reason = f"LSTM deviation {deviation:.3f} exceeds threshold"
                anomalies.append((original_index, original_price, reason))

        return anomalies
