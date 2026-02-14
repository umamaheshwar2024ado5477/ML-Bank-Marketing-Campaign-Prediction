import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, matthews_corrcoef
import joblib
import os

# Create models directory
if not os.path.exists('models'):
    os.makedirs('models')

# Load Dataset
print("Loading dataset...")
df = pd.read_csv('bank-full.csv', sep=';')

# Separate features and target
X = df.drop('y', axis=1)
y = df['y']

# Encode target
le = LabelEncoder()
y = le.fit_transform(y)
joblib.dump(le, 'models/label_encoder.pkl')

# Identiy categorical and numerical columns
categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

print(f"Categorical columns: {list(categorical_cols)}")
print(f"Numerical columns: {list(numerical_cols)}")

# Preprocessing Pipeline
# We need to handle categorical variables. OneHotEncoding is standard.
# We also need to scale numerical variables.

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models Dictionary
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "Naive Bayes": GaussianNB(), # GaussianNB doesn't support sparse input well sometimes, might need dense
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
}

# Training and Evaluation
results = []

# GaussianNB requires dense matrix, others can handle sparse (from OneHotEncoder)
# We will create a pipeline for each.

import warnings
warnings.filterwarnings('ignore')

print("\nTraining models...")

best_model_name = ""
best_model_score = -1

for name, model in models.items():
    print(f"Training {name}...")
    
    # Create pipeline
    # GaussianNB requires toarray() if output is sparse. 
    # But ColumnTransformer returns sparse by default if OneHotEncoder does.
    # We can force sparse_threshold=0 in ColumnTransformer or convert in a custom transformer.
    
    if name == "Naive Bayes":
         # Use a slightly different preprocessor or ensure dense
         # Re-define preprocessor for NB to return dense
         nb_preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols)
            ])
         clf = Pipeline(steps=[('preprocessor', nb_preprocessor),
                              ('classifier', model)])
    else:
         clf = Pipeline(steps=[('preprocessor', preprocessor),
                              ('classifier', model)])
    
    clf.fit(X_train, y_train)
    
    # Predictions
    y_pred = clf.predict(X_test)
    y_prob = clf.predict_proba(X_test)[:, 1] if hasattr(clf, "predict_proba") else None
    
    # Metrics
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob) if y_prob is not None else 0
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    mcc = matthews_corrcoef(y_test, y_pred)
    
    results.append({
        "Model": name,
        "Accuracy": acc,
        "AUC": auc,
        "Precision": prec,
        "Recall": rec,
        "F1 Score": f1,
        "MCC": mcc
    })
    
    # Save model
    joblib.dump(clf, f'models/{name.replace(" ", "_")}.pkl')
    
    if auc > best_model_score:
        best_model_score = auc
        best_model_name = name

# Create DataFrame for results
results_df = pd.DataFrame(results)
print("\nEvaluation Results:")
print(results_df)

# Save results
results_df.to_csv('model_results.csv', index=False)
print("\nModels and results saved.")
