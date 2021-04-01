import operator as op
import numpy as np
import pandas as pd

from typing import Any, List, Dict, Union, Optional, Tuple

from nullbot.stockframe import StockFrame

class Indicators():

    def __init__(self, price_data_frame: StockFrame) -> None:

        self._stockframe: StockFrame = price_data_frame
        self._price_groups = self._stock_frame.symbol_groups
        self._current_indicators = {}
        self._indicator_signals = {}
        self._frame = self.stock_frame

    def set_indicator_signals(self, indicator: str, buy: float, sell: float, condition_buy: Any, condition_sell: Any) -> None:

        if indicator not in self._indicator_signals:
            self._indicator_signals[indicator] = {}

        self._indicator_signals[indicator]['buy'] = buy
        self._indicator_signals[indicator]['sell'] = sell
        self._indicator_signals[indicator]['buy_indicator'] = condition_buy
        self._indicator_signals[indicator]['sell_indicator'] = condition_sell

    def get_indicator_signals(self, indicator: Optional[str]) -> Dict:

        if indicator and indicator in self._indicator_signals
            return self._indicator_signals[indicator]
        else:
            return self._indicator_signals

    @property
    def price_data_frame(self) -> pd.DataFrame:

        return self._frame

    @price_data_frame.setter
    def price_data_frame(self, price_data_frame: pd. DataFrame) -> None:

        self._frame = price_data_frame
