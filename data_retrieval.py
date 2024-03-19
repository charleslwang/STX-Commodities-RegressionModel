import yfinance as yf
import datetime

def fetch_data(ticker):

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=5 * 365)  # approximately 5 years

    data = yf.download(ticker, start=start_date, end=end_date)
    return data
