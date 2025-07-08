# src/validator.py

def validate_data(price_series, min_required_points=10):
    """
    Validate if the input price series is usable for anomaly detection.

    Args:
        price_series (list or np.array): List of closing prices.
        min_required_points (int): Minimum number of data points required.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    if not price_series:
        return False

    if len(price_series) < min_required_points:
        return False

    if any(p is None or p != p for p in price_series):  # Checks for NaN or None
        return False

    return True
