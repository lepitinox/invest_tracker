""" track a single stock """
from typing import Tuple


class SingleStock:

    def __init__(self, symbol: str, country: str, devise: str = "EUR"):
        self.symbol = symbol
        self.country = country
        self.devise = devise

    def get_prices(self, time_range: Tuple[str, str]):
        """
        get prices from investing api

        Parameters
        ----------
        time_range

        Returns
        -------

        """
        pass


