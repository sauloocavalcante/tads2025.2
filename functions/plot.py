import plotly.express as px
from plotly.graph_objects import Figure
from functions.download import download_data

def plot_ts(ticker:str) -> Figure:
    """
    Generates an interactive time-series line chart for a given financial ticker.

    This function fetches historical market data via the 'download_data' utility 
    and renders a visualization of the 'Close' prices over time.

    Args:
        ticker (str): The stock or asset symbol to download (e.g., 'AAPL', 'TSLA', 'BTC-USD').

    Returns:
        Figure: A Plotly Figure object containing the interactive line chart.
    """
    df = download_data(ticker)

    fig = px.line(
        df,
        x = 'Date',
        y = 'Close',
        title = f'{ticker} Stock Price'
    )

    return fig
