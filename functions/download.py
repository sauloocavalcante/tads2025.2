import yfinance as yf
import pandas as pd

def download_data(ticker:str = 'TSLA') -> pd.DataFrame:
    """
    Downloads historical market data for a given ticker from Yahoo Finance.

    Args:
        ticker (str): The stock symbol to download (e.g., 'AAPL', 'BTC-USD'). 
            Defaults to 'TSLA'.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the historical data 
            (Open, High, Low, Close, Adj Close, Volume) with a reset index.
    """

    df = yf.download(
        ticker,
        period='max',
        multi_level_index=False
        ).reset_index()
    
    return df
