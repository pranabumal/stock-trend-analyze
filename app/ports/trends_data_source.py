from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd


class TrendsDataSource(ABC):
    @abstractmethod
    def get_interest(self, keyword: str, start: datetime, end: datetime) -> pd.DataFrame:
        raise NotImplementedError
