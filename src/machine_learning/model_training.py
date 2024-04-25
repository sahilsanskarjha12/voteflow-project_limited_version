import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def generate_training_data(n_samples=1000, n_features=20, n_classes=2, random_state=42):
    """Generate synthetic training data for demonstration."""
    X, y = make_classification(n_samples=n_samples, n_features=n_features, n_classes=n_classes, random_state=random_state)
    return X, y

def train_model(X_train, y_train, model):
    """Train a machine learning model on the training data."""
    # Train the model on the training data
    model.fit(X_train, y_train)

    return model

if __name__ == "__main__":
    # Generate synthetic training data
    X_train, y_train = generate_training_data()

    # Initialize the model
    model = RandomForestClassifier(random_state=42)

    # Train the model on the training data
    trained_model = train_model(X_train, y_train, model)

    print("Model training completed successfully!")
