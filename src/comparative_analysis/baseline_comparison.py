# src/baseline_comparison.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(file_path):
    """Load dataset from file."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess dataset."""
    # Add preprocessing steps as needed
    return df

def split_data(df):
    """Split dataset into features and target."""
    X = df.drop(columns=['target_column'])
    y = df['target_column']
    return X, y

def train_model(X_train, y_train):
    """Train machine learning model."""
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

def main():
    # Load and preprocess datasets
    baseline_data = load_data('baseline_data.csv')
    voteflow_data = load_data('voteflow_data.csv')

    baseline_data = preprocess_data(baseline_data)
    voteflow_data = preprocess_data(voteflow_data)

    # Split datasets into features and target
    X_baseline, y_baseline = split_data(baseline_data)
    X_voteflow, y_voteflow = split_data(voteflow_data)

    # Split data into training and testing sets
    X_train_baseline, X_test_baseline, y_train_baseline, y_test_baseline = train_test_split(X_baseline, y_baseline, test_size=0.2, random_state=42)
    X_train_voteflow, X_test_voteflow, y_train_voteflow, y_test_voteflow = train_test_split(X_voteflow, y_voteflow, test_size=0.2, random_state=42)

    # Train machine learning models
    model_baseline = train_model(X_train_baseline, y_train_baseline)
    model_voteflow = train_model(X_train_voteflow, y_train_voteflow)

    # Evaluate model performance
    accuracy_baseline = evaluate_model(model_baseline, X_test_baseline, y_test_baseline)
    accuracy_voteflow = evaluate_model(model_voteflow, X_test_voteflow, y_test_voteflow)

    # Compare performance
    print("Baseline Model Accuracy:", accuracy_baseline)
    print("VoteFlow Model Accuracy:", accuracy_voteflow)

if __name__ == "__main__":
    main()
