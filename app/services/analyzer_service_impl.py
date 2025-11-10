from __future__ import annotations

from datetime import datetime, timedelta
import pandas as pd

from app.ports.analyzer_service import AnalyzerService
from app.ports.stock_data_source import StockDataSource
from app.ports.trends_data_source import TrendsDataSource


class AnalyzerServiceImpl(AnalyzerService):
    def __init__(self, stocks: StockDataSource, trends: TrendsDataSource):
        self.stocks = stocks
        self.trends = trends

    def analyze(self, symbol: str, keyword: str, days: int):
        end = datetime.now()
        start = end - timedelta(days=days)

        price_df = self.stocks.get_prices(symbol, start, end)
        trend_df = self.trends.get_interest(keyword, start, end)

        def _normalize_index(df: pd.DataFrame) -> pd.DataFrame:
            if df is None or df.empty:
                return df
            idx = pd.to_datetime(df.index)
            try:
                if getattr(idx, "tz", None) is not None:
                    idx = idx.tz_convert(None)
            except Exception:
                try:
                    idx = idx.tz_localize(None)
                except Exception:
                    pass
            df = df.copy()
            df.index = idx.normalize()
            return df

        price_df = _normalize_index(price_df)
        trend_df = _normalize_index(trend_df)

        if price_df is not None and not price_df.empty and not isinstance(price_df.index, pd.DatetimeIndex):
            price_df.index = pd.to_datetime(price_df.index)
        if trend_df is not None and not trend_df.empty and not isinstance(trend_df.index, pd.DatetimeIndex):
            trend_df.index = pd.to_datetime(trend_df.index)

        price_daily = price_df.resample("D").last() if price_df is not None and not price_df.empty else pd.DataFrame(columns=["price"])  # type: ignore
        trend_daily = trend_df.resample("D").mean() if trend_df is not None and not trend_df.empty else pd.DataFrame(columns=["interest"])  # type: ignore

        daily_index = pd.date_range(start=start.date(), end=end.date(), freq="D")
        price_daily = price_daily.reindex(daily_index).ffill()
        trend_daily = trend_daily.reindex(daily_index).ffill()

        df = pd.concat([price_daily, trend_daily], axis=1).dropna()
        corr = df["price"].corr(df["interest"]) if len(df) > 1 else 0.0
        return df, float(corr)

