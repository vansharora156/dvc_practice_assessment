import os
import sys
import pickle
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def main():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)["train"]
        
    input_file = "data/processed.csv"
    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)
        
    df = pd.read_csv(input_file)
    
    # Target selection
    target_col = 'target' if 'target' in df.columns else 'Survived'
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=params['test_size'], 
        random_state=params['random_state']
    )
    
    model = RandomForestClassifier(
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        random_state=params['random_state']
    )
    model.fit(X_train, y_train)
    
    os.makedirs("models", exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)
        
    # Save test dataset for evaluation
    test_df = X_test.copy()
    test_df['target'] = y_test
    test_df.to_csv("data/test.csv", index=False)
    
    print(f"Model trained successfully and saved to models/model.pkl")
    print(f"Test split saved to data/test.csv with {len(test_df)} samples")

if __name__ == '__main__':
    main()
