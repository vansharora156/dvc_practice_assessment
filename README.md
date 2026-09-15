# DVC Class Assessment — Practical Tasks Implementation

This repository contains the complete implementation for **Part B: Practical DVC Tasks** (Tasks 1 through 5).

---

## Workspace Structure

```
DVC/
├── .dvc/                   # DVC tracking directory
├── dvc-storage/            # Local DVC Remote directory (Task 2)
├── data/
│   ├── titanic.csv         # Raw Titanic dataset (DVC tracked)
│   ├── winequality.csv     # Raw Wine Quality dataset (DVC tracked)
│   ├── processed.csv       # Preprocessed dataset output
│   └── test.csv            # Evaluation test split
├── src/
│   ├── generate_datasets.py# Dataset generation helper
│   ├── preprocess.py       # Data cleaning stage
│   ├── train.py            # Model training stage
│   └── evaluate.py         # Model evaluation stage
├── models/
│   └── model.pkl           # Trained model artifact
├── dvc.yaml                # DVC pipeline definition
├── dvc.lock                # DVC stage execution lockfile
├── params.yaml             # Hyperparameters configuration
├── metrics.json            # Model evaluation metrics output
└── DVC_Assessment_Solutions.md  # Answers for Part A & Task 4
```

---

## Tasks Overview & Quick Run

### Environment Setup
Activate virtual environment and verify installations:
```bash
.\venv\Scripts\activate
git status
dvc status
```

### Task 1: Track Datasets with DVC
```bash
dvc add data/titanic.csv
git add data/titanic.csv.dvc data/.gitignore
git commit -m "Track titanic dataset with DVC"
```

### Task 2: DVC Remote Operations
```bash
dvc remote add -d localremote dvc-storage
dvc push
# Simulate file loss and recovery:
rm data/titanic.csv
dvc pull
```

### Task 3 & 4: Data Pipeline & Change Detection
```bash
dvc repro
dvc status
```

### Task 5: ML Pipeline, Parameter Tuning & Metrics
```bash
dvc repro
dvc dag
dvc metrics show
```
