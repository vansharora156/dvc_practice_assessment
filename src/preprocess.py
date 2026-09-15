import argparse
import os
import pandas as pd
import numpy as np

def preprocess_titanic(df):
    # Drop unnecessary columns
    drop_cols = [c for c in ['PassengerId', 'Name', 'Ticket', 'Cabin'] if c in df.columns]
    df = df.drop(columns=drop_cols)
    
    # Handle missing values
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    if 'Fare' in df.columns:
        df['Fare'] = df['Fare'].fillna(df['Fare'].median())
        
    # Encode categorical variables
    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    if 'Embarked' in df.columns:
        df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
        
    return df

def preprocess_wine(df):
    # Fill missing values if any
    df = df.fillna(df.median(numeric_only=True))
    
    # Convert quality into binary target (1 if quality >= 6 else 0) for classification
    if 'quality' in df.columns:
        df['target'] = (df['quality'] >= 6).astype(int)
        df = df.drop(columns=['quality'])
        
    return df

def main():
    parser = argparse.ArgumentParser(description="Preprocess data for DVC pipeline")
    parser.add_argument('--input', type=str, default='data/winequality.csv', help='Input CSV path')
    parser.add_argument('--output', type=str, default='data/processed.csv', help='Output CSV path')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file not found at {args.input}")

    print(f"Reading raw data from {args.input}...")
    df = pd.read_csv(args.input)
    
    if 'PassengerId' in df.columns or 'Survived' in df.columns:
        df_processed = preprocess_titanic(df)
    else:
        df_processed = preprocess_wine(df)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df_processed.to_csv(args.output, index=False)
    print(f"Successfully processed data saved to {args.output}. Shape: {df_processed.shape}")

if __name__ == '__main__':
    print("[Task 4 Logger] Preprocessing execution initiated...")
    main()