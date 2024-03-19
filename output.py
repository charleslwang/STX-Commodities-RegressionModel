import matplotlib.pyplot as plt
import pandas as pd

def display_results(historical_data, predictions, ticker):
    """
    Display the historical data and predictions in a readable format and plot a graph.

    Parameters:
    historical_data (pandas.DataFrame): The historical data for the ticker.
    predictions (numpy.ndarray): The predicted values for the future.
    ticker (str): The ticker symbol for the stock or commodity.
    """
    print(f"Results for {ticker}:")
    print("\nHistorical Data:")
    print(historical_data.tail())  # Show the last few rows of historical data

    # Assuming the predictions are for future dates, create a date range for these predictions
    future_dates = pd.date_range(start=historical_data.index[-1], periods=len(predictions) + 1, freq='B')[1:]
    predictions_df = pd.DataFrame(predictions, index=future_dates, columns=['Predictions'])

    print("\nPredictions for the next period:")
    print(predictions_df.head())  # Show the first few rows of predictions

    plot_results(historical_data, predictions_df, ticker)

def plot_results(historical_data, predictions_df, ticker):
    """
    Plot the historical data and predictions.

    Parameters:
    historical_data (pandas.DataFrame): The historical data for the ticker.
    predictions_df (pandas.DataFrame): The predictions as a DataFrame.
    ticker (str): The ticker symbol for the stock or commodity.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(historical_data.index, historical_data['Close'], label='Historical Data')
    plt.plot(predictions_df.index, predictions_df['Predictions'], label='Predictions', linestyle='--')
    plt.title(f"Price Forecast for {ticker}")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
