from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd


class StockDataSource(ABC):
    """Port for fetching stock price time series."""

    @abstractmethod
    def get_prices(self, symbol: str, start: datetime, end: datetime) -> pd.DataFrame:
        """
        Return a DataFrame indexed by datetime with a single column named 'price'.
        Missing values should be left as-is; the service layer decides how to fill/drop.
        """
        raise NotImplementedError
