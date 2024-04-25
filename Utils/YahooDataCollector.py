import yfinance as yf
import plotly.graph_objs as go


class YahooDataCollector(yf.Ticker):
    def __init__(self, stock_name) -> None:
        self.ticker = yf.Ticker(stock_name)
        self.stock_name = stock_name
        self.general_info = self.ticker.info
        self.hist = yf.download(self.stock_name).dropna()

    def filter_financial_factors(self):
        metadata = self.info
        financial_factors = {
            "sector": metadata.get("sector", ""),
            "industry": metadata.get("industry", ""),
            "marketCap": metadata.get("marketCap", ""),
            "trailingPE": metadata.get("trailingPE", ""),
            "forwardPE": metadata.get("forwardPE", ""),
            "dividendRate": metadata.get("dividendRate", ""),
            "dividendYield": metadata.get("dividendYield", ""),
            "52WeekChange": metadata.get("52WeekChange", ""),
            "SandP52WeekChange": metadata.get("SandP52WeekChange", ""),
            "returnOnAssets": metadata.get("returnOnAssets", ""),
            "returnOnEquity": metadata.get("returnOnEquity", ""),
            "earningsGrowth": metadata.get("earningsGrowth", ""),
            "revenueGrowth": metadata.get("revenueGrowth", ""),
            "grossMargins": metadata.get("grossMargins", ""),
            "ebitdaMargins": metadata.get("ebitdaMargins", ""),
            "operatingMargins": metadata.get("operatingMargins", ""),
            "pegRatio": metadata.get("pegRatio", ""),
            "totalCash": metadata.get("totalCash", ""),
            "totalDebt": metadata.get("totalDebt", ""),
            "freeCashflow": metadata.get("freeCashflow", ""),
            "operatingCashflow": metadata.get("operatingCashflow", ""),
            "enterpriseValue": metadata.get("enterpriseValue", ""),
            "trailingPegRatio": metadata.get("trailingPegRatio", ""),
            "dividends": metadata.get("dividends", ""),
            "splits": metadata.get("splits", ""),
            "bonus": metadata.get("bonus", "")
        }
        return financial_factors
    def get_historical_prices(self, interval='1d'):
        try:
            # Fetch historical data with specified interval
            stock_data = yf.download(self.stock_name, interval=interval)
            return stock_data
        except Exception as e:
            print(f"Error fetching historical prices for {self.stock_name}: {e}")
            return None
        
    def plot_stock_prices(self, stock_symbol = None, interval='1d'):
        if not stock_symbol:
            stock_symbol = self.stock_name
        try:
            # Fetch historical data with specified interval
            stock_data = yf.download(stock_symbol, interval=interval)
            if stock_data.empty:
                print(f"No data available for {stock_symbol} with interval {interval}")
                return
        except Exception as e:
            print(f"Error fetching historical prices for {stock_symbol}: {e}")
            return
        self.plot_given_df(stock_data)
        
    def plot_given_df(self, stock_data):
        # Create traces for Candlestick chart
        trace = go.Candlestick(x=stock_data.index,
                            open=stock_data['Open'],
                            high=stock_data['High'],
                            low=stock_data['Low'],
                            close=stock_data['Close'])

        layout = go.Layout(title=f"Historical Prices",
                        xaxis=dict(title='Date'),
                        yaxis=dict(title='Price'))

        # Create figure and add traces
        fig = go.Figure(data=[trace], layout=layout)

        # Show interactive plot
        fig.show()
        

if __name__ == "__main__":
    # Example usage
    stock_name = "AAPL"  # Example stock symbol
    stock = YahooDataCollector(stock_name)
    prices = stock.get_historical_prices()
    print(prices)
    stock.plot_stock_prices()

    
    
