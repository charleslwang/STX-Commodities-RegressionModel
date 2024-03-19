from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

def prepare_data(data):
    """
    Prepares the data for modeling, extracting features and target.

    Parameters:
    data (pandas.DataFrame): The historical data for the ticker.

    Returns:
    X (numpy.ndarray): The feature matrix.
    y (numpy.ndarray): The target variable.
    """
    # For a simple linear regression, we might just use time as a feature
    # Convert index to a numeric value (e.g., days since start)
    X = np.arange(len(data)).reshape(-1, 1)
    y = data['Close'].values  # Assuming 'Close' is the target

    return X, y

def train_model(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Mean Squared Error: {mse}")

    return model

def predict(model, X):
    future_predictions = model.predict(X)
    return future_predictions