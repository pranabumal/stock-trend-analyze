from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd


class AnalyzerService(ABC):
    @abstractmethod
    def analyze(self, symbol: str, keyword: str, days: int) -> Tuple[pd.DataFrame, float]:
        """Return combined dataframe with columns 'price' and 'interest' and their correlation."""
        raise NotImplementedError
