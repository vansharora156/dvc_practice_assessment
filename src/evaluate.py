import os
import json
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

def main():
    model_path = "models/model.pkl"
    test_path = "data/test.csv"
    metrics_path = "metrics.json"
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
        
    test_df = pd.read_csv(test_path)
    X_test = test_df.drop(columns=['target'])
    y_test = test_df['target']
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='binary')
    precision = precision_score(y_test, y_pred, average='binary')
    recall = recall_score(y_test, y_pred, average='binary')
    
    metrics = {
        "accuracy": round(float(accuracy), 4),
        "f1_score": round(float(f1), 4),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4)
    }
    
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)
        
    print(f"Evaluation complete. Metrics saved to {metrics_path}: {metrics}")

if __name__ == '__main__':
    main()
