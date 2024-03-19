import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data):

    # Fill missing values
    data = data.fillna(method='ffill')  # forward filling to replace missing values with the last known value

    # # Normalize data using MinMaxScaler
    # scaler = MinMaxScaler(feature_range=(0, 1))
    # scaled_data = scaler.fit_transform(data[['Open', 'High', 'Low', 'Close', 'Volume']])
    #
    # # Convert the scaled data back to a DataFrame
    # processed_data = pd.DataFrame(scaled_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'], index=data.index)

    return data[['Close']]
