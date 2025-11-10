from __future__ import annotations

import os
from datetime import datetime
import pandas as pd
import requests

from app.ports.stock_data_source import StockDataSource


class AlphaVantageClient(StockDataSource):
    """Alpha Vantage implementation of StockDataSource.

    Only daily close prices are fetched. Consumers should slice date range.
    """

    def __init__(self, api_key: str | None = None, timeout: int = 10):
        self.api_key = api_key or os.getenv("ALPHAVANTAGE_API_KEY")
        self.timeout = timeout

    def get_prices(self, symbol: str, start: datetime, end: datetime) -> pd.DataFrame:
        if not self.api_key:
            raise ValueError("Alpha Vantage API key missing. Set ALPHAVANTAGE_API_KEY or pass api_key.")
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key,
            "outputsize": "full",
        }
        resp = requests.get(url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json().get("Time Series (Daily)", {})
        if not data:
            return pd.DataFrame(columns=["price"])  # empty
        df = pd.DataFrame.from_dict(data, orient="index")
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={"4. close": "price"})
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        df = df.sort_index()
        return df.loc[start:end, ["price"]]
