import argparse
import numpy as np
from data_retrieval import fetch_data
from data_preprocessing import preprocess_data
from model_development import prepare_data, train_model, predict
from output import display_results

def main(ticker):
    # Step 1: Data Retrieval
    print(f"Fetching historical data for {ticker}...")
    historical_data = fetch_data(ticker)

    # Step 2: Data Preprocessing
    print("Preprocessing data...")
    processed_data = preprocess_data(historical_data)

    # Data preparation for model
    X, y = prepare_data(processed_data)  # Separate features and target

    # Step 3: Model Development
    print("Training model...")
    model = train_model(X, y)  # Pass both features and target to the model

    # Step 4: Prediction
    print("Predicting future performance...")
    # Assume you prepare future X data for prediction (future_dates_X)
    future_dates_X = np.arange(len(processed_data) + len(y), len(processed_data) + 2 * len(y)).reshape(-1, 1)
    future_predictions = predict(model, future_dates_X)

    # Step 5: Display Results
    print("Displaying results...")
    display_results(historical_data, future_predictions, ticker)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stock and Commodity Market Prediction Tool")
    parser.add_argument('ticker', type=str, help='Ticker symbol for the market to predict')

    args = parser.parse_args()
    main(args.ticker)