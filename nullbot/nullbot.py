import pandas as pdb

from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datatime import datatime, time, timezone

from typing import List, Dict, Union

class PyNullbot():

    def __init__(self, client_id: str, redirect_uri: str, credentials_path: str = None, trading_account: str = None) -> None:

        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credentials_path: str = credentials_path
        self.session: TDClient = self.__create_session()
        self.trades: dict = {}
        self.historical_prices: dict = {}
        self.stock_frame = None

    def _create_session(self) -> TDClient:
        TDClient = TDClient(
        client_id=self.client_id,
        redirect_uri=self.redirect_uri,
        credentials_path=self.credentials_path
        )

        td_client.login()

        return td_client

# refactor later to be generalized and pass in market open data from list

    @property
    def us_premarket_open(self) -> bool:
        now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        us_premarket_start_time = datetime.now().replace(hour=12, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        us_premarket_end_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()

        if us_premarket_start_time >= now >= us_premarket_end_time:
            return True
        else:
            return False

    @property
    def us_market_open(self) -> bool:
        now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        us_market_start_time = datetime.now().replace(hour=13, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        us_market_end_time = datetime.now().replace(hour=00, minute=00, second=00, tzinfo=timezone.utc).timestamp()
        
        if us_market_start_time >= now >= us_market_end_time:
            return True
        else:
            return False

    @property
    def us_postmarket_open(self) -> bool:
        now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        us_postmarket_start_time = datetime.now().replace(hour=22, minute=30, second=00, tzinfo=timezone.utc).timestamp()
        us_postmarket_end_time = datetime.now().replace(hour=20, minute=00, second=00, tzinfo=timezone.utc).timestamp()

        if us_postmarket_start_time >= now >= us_postmarket_end_time:
            return True
        else:
            return False

    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def get_current_quotes(self) -> dict:
        pass

    def get_historical_prices(self) -> List[Dict]:
        pass
