from __future__ import annotations

import os

from app.infrastructure.mock_sources import MockStockSource, MockTrendsSource
from app.infrastructure.alpha_vantage_client import AlphaVantageClient
try:
    from app.infrastructure.pytrends_client import PyTrendsClient
except Exception:
    PyTrendsClient = None  # optional
from app.services.analyzer_service_impl import AnalyzerServiceImpl


def get_analyzer_service(use_mock: bool | None = None) -> AnalyzerServiceImpl:
    """Factory for AnalyzerServiceImpl.

    - If use_mock is True, always return mocks.
    - If use_mock is False, try real providers; on any error, fall back to mocks.
    - If use_mock is None, read USE_MOCK env (default true).
    """
    if use_mock is None:
        use_mock = os.getenv("USE_MOCK", "true").lower() == "true"

    if use_mock:
        return AnalyzerServiceImpl(stocks=MockStockSource(), trends=MockTrendsSource())

    # Validate real providers before wiring
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    if not api_key:
        return AnalyzerServiceImpl(stocks=MockStockSource(), trends=MockTrendsSource())

    if PyTrendsClient is None:
        return AnalyzerServiceImpl(stocks=MockStockSource(), trends=MockTrendsSource())

    # All good: build real providers
    stocks = AlphaVantageClient(api_key=api_key)
    trends = PyTrendsClient()
    return AnalyzerServiceImpl(stocks=stocks, trends=trends)
