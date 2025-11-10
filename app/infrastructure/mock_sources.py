from __future__ import annotations

from datetime import datetime, timedelta
import random
import numpy as np
import pandas as pd

from app.ports.stock_data_source import StockDataSource
from app.ports.trends_data_source import TrendsDataSource


class MockStockSource(StockDataSource):
    def get_prices(self, symbol: str, start: datetime, end: datetime) -> pd.DataFrame:
        days = (end.date() - start.date()).days + 1
        dates = pd.date_range(start=start, periods=days, freq="D")
        base_price = 100 + hash(symbol) % 100
        prices = []
        current = float(base_price)
        for _ in range(days):
            change = (random.random() - 0.48) * 3
            current = max(1.0, current * (1 + change / 100))
            prices.append(current)
        return pd.DataFrame({"price": prices}, index=dates)


class MockTrendsSource(TrendsDataSource):
    def get_interest(self, keyword: str, start: datetime, end: datetime) -> pd.DataFrame:
        days = (end.date() - start.date()).days + 1
        dates = pd.date_range(start=start, periods=days, freq="D")
        base_trend = 40 + hash(keyword) % 30
        trends = []
        for i, date in enumerate(dates):
            day_effect = -15 if date.weekday() >= 5 else 5
            monthly_cycle = 20 * np.sin(2 * np.pi * i / 30)
            spike = 40 + random.random() * 30 if random.random() < 0.03 else 0
            noise = (random.random() - 0.5) * 20
            val = base_trend + day_effect + monthly_cycle + spike + noise
            trends.append(max(0.0, min(100.0, val)))
        return pd.DataFrame({"interest": trends}, index=dates)
