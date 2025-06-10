import argparse
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import pickle
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Parameterization
parser = argparse.ArgumentParser()
parser.add_argument('--n_estimators', type=int, default=100)
parser.add_argument('--random_state', type=int, default=42)
parser.add_argument('--test_size', type=float, default=0.2)
parser.add_argument('--data_path', type=str, default='datasets/diabetes.csv')
parser.add_argument('--model_path', type=str, default='saved models/diabetes_model.sav')
args = parser.parse_args()

# 1. Load data
df = pd.read_csv('datasets/diabetes.csv')
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)

# 5. Log with MLflow
with mlflow.start_run(run_name="Diabetes Pipeline"):
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("precision", prec)
    mlflow.log_metric("recall", rec)
    mlflow.sklearn.log_model(model, "model", input_example=X_test.iloc[:1])
    print(f"Logged: accuracy={acc}, precision={prec}, recall={rec}")


    # --- Automated reporting ---
    # Classification report
    report = classification_report(y_test, y_pred)
    with open("classification_report.txt", "w") as f:
        f.write(report)
    mlflow.log_artifact("classification_report.txt")

    # Confusion matrix plot
    disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    plt.title("Confusion Matrix")
    plt.savefig("confusion_matrix.png")
    mlflow.log_artifact("confusion_matrix.png")
    plt.close()

# 6. (Optional) Save model as .sav for later use
with open('saved models/diabetes_model.sav', 'wb') as f:
    pickle.dump(model, f)