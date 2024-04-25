# baseline_model/src/train_baseline_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

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

def save_model(model, file_path):
    """Save trained model to file."""
    joblib.dump(model, file_path)

def main():
    # Load and preprocess dataset
    data = load_data('data/baseline_training_data.csv')
    data = preprocess_data(data)
    
    # Split dataset into features and target
    X, y = split_data(data)
    
    # Train machine learning model
    model = train_model(X, y)
    
    # Save trained model
    save_model(model, 'models/baseline_model.pkl')

if __name__ == "__main__":
    main()
