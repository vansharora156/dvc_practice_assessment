import os
import pandas as pd
import numpy as np

def generate_titanic_dataset(output_path="data/titanic.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    np.random.seed(42)
    n_samples = 200
    
    passenger_ids = np.arange(1, n_samples + 1)
    pclasses = np.random.choice([1, 2, 3], size=n_samples, p=[0.25, 0.25, 0.5])
    sexes = np.random.choice(['male', 'female'], size=n_samples, p=[0.6, 0.4])
    ages = np.random.choice([np.nan, 22.0, 38.0, 26.0, 35.0, 54.0, 2.0, 27.0, 14.0, 4.0], size=n_samples)
    sibsp = np.random.choice([0, 1, 2, 3], size=n_samples, p=[0.7, 0.2, 0.05, 0.05])
    parch = np.random.choice([0, 1, 2], size=n_samples, p=[0.8, 0.15, 0.05])
    fares = np.round(np.random.exponential(scale=32.0, size=n_samples), 2)
    embarked = np.random.choice(['S', 'C', 'Q', np.nan], size=n_samples, p=[0.7, 0.2, 0.08, 0.02])
    
    # Calculate survival probability based on features
    survived_prob = 0.3 + 0.3 * (sexes == 'female') + 0.2 * (pclasses == 1) - 0.1 * (pclasses == 3)
    survived_prob = np.clip(survived_prob, 0, 1)
    survived = np.random.binomial(1, survived_prob)
    
    df = pd.DataFrame({
        'PassengerId': passenger_ids,
        'Survived': survived,
        'Pclass': pclasses,
        'Name': [f'Passenger_{i}' for i in passenger_ids],
        'Sex': sexes,
        'Age': ages,
        'SibSp': sibsp,
        'Parch': parch,
        'Ticket': [f'TICK_{i*100}' for i in passenger_ids],
        'Fare': fares,
        'Cabin': [f'C{i}' if i % 4 == 0 else np.nan for i in passenger_ids],
        'Embarked': embarked
    })
    
    df.to_csv(output_path, index=False)
    print(f"Generated Titanic dataset at {output_path} with {len(df)} records.")

def generate_wine_dataset(output_path="data/winequality.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    np.random.seed(42)
    n_samples = 300
    
    df = pd.DataFrame({
        'fixed_acidity': np.round(np.random.normal(8.3, 1.7, n_samples), 2),
        'volatile_acidity': np.round(np.random.normal(0.52, 0.18, n_samples), 3),
        'citric_acid': np.round(np.random.uniform(0.0, 0.75, n_samples), 2),
        'residual_sugar': np.round(np.random.exponential(2.5, n_samples), 2),
        'chlorides': np.round(np.random.normal(0.087, 0.047, n_samples), 3),
        'free_sulfur_dioxide': np.round(np.random.uniform(5, 50, n_samples)),
        'total_sulfur_dioxide': np.round(np.random.uniform(20, 150, n_samples)),
        'density': np.round(np.random.normal(0.996, 0.002, n_samples), 4),
        'pH': np.round(np.random.normal(3.31, 0.15, n_samples), 2),
        'sulphates': np.round(np.random.normal(0.65, 0.17, n_samples), 2),
        'alcohol': np.round(np.random.uniform(8.4, 14.0, n_samples), 1),
        'quality': np.random.choice([3, 4, 5, 6, 7, 8], size=n_samples, p=[0.05, 0.1, 0.4, 0.3, 0.1, 0.05])
    })
    
    df.to_csv(output_path, index=False)
    print(f"Generated Wine Quality dataset at {output_path} with {len(df)} records.")

if __name__ == '__main__':
    generate_titanic_dataset()
    generate_wine_dataset()
