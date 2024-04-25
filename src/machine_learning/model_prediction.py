def make_predictions(model, new_data):
    """Make predictions using a trained machine learning model on new data."""
    # Predict outcomes for new data
    predictions = model.predict(new_data)

    return predictions

# Example usage
if __name__ == "__main__":
    import numpy as np
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    # Generate synthetic data for demonstration
    X_train, y_train = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    X_new, _ = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on new data
    new_data_predictions = make_predictions(model, X_new)
    print("Predictions on new data:", new_data_predictions)
