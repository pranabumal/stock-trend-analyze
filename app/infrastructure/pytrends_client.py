from __future__ import annotations

from datetime import datetime
import pandas as pd

try:
    from pytrends.request import TrendReq
except Exception:  # pragma: no cover - optional dependency
    TrendReq = None

from app.ports.trends_data_source import TrendsDataSource


class PyTrendsClient(TrendsDataSource):
    def __init__(self, hl: str = "en-US", tz: int = 0):
        if TrendReq is None:
            raise ImportError("pytrends is not installed. Add it to requirements and install.")
        self.pytrends = TrendReq(hl=hl, tz=tz)

    def get_interest(self, keyword: str, start: datetime, end: datetime) -> pd.DataFrame:
        timeframe = f"{start.strftime('%Y-%m-%d')} {end.strftime('%Y-%m-%d')}"
        self.pytrends.build_payload([keyword], timeframe=timeframe)
        df = self.pytrends.interest_over_time()
        if df is None or df.empty:
            return pd.DataFrame(columns=["interest"])  # empty
        df = df.rename(columns={keyword: "interest"})
        return df[["interest"]]
