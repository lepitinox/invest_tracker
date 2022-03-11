""" collection of tools to help the use of investpy """
from typing import Tuple

import investpy
import investpy as sp
import pandas as pd


def isin_to_symbol(isin: str, country: str = "france"):
    """
    Use the search engine of investing to find the symbol corresponding to the isin

    If isin not in database, will return None and print a Warning

    Parameters
    ----------
    isin : str
        the isin code (ISO 6166)
    country : str
        Country of the marketplace

    Returns
    -------
    Union[None, str]
        returns None if no match else returns the symbol
    """
    try:
        data = sp.search_stocks("isin", isin)
    except RuntimeError as e:
        print(f"Isin : {isin} is not in investing database ({e})")
        return None
    if country in data["country"]:
        return data[data["country"] == "france"]["symbol"].values[0]
    return None


def get_prices_from_symbol(symbol: str, country: str, date_range: Tuple[str, str]):
    """
    use investing api to request prices of a stock during a date range

    if encounter an error during request to api will print it and return a empty DataFrame

    Parameters
    ----------
    country : str
        country of marketplace
    symbol : str
        Symbol of Stock
    date_range : str
        time range on witch requesting data

    Returns
    -------
    Union[pd.DataFrame, None]

    """
    try:
        df = investpy.get_stock_historical_data(symbol, country, date_range[0], date_range[1])
    except Exception as e:
        if e is RuntimeError:
            print(f"Warning : symbol ({symbol}) not in database : {e}")
            return pd.DataFrame()
        elif e is IndexError:
            print(f"Warning : requested date range is not in database")
            return None
        else:
            print(e)
            return pd.DataFrame()
    if df.index[0] > pd.to_datetime(date_range[0]):
        print(f"Warning : minimun requested date ({date_range[0]}) is not in database, using {df.index[0]}")
    return df


def get_prices_from_isin(isin: str, date_range: Tuple[str, str], country: str = "france"):
    symbol = isin_to_symbol(isin, country)
    if symbol is None:
        return pd.DataFrame()
    return get_prices_from_symbol(symbol, country, date_range)

