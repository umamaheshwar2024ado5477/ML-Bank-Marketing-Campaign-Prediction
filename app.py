import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Set page configuration
st.set_page_config(page_title="Bank Marketing Prediction", layout="wide")

st.title("Bank Marketing Campaign Prediction")
st.markdown("""
This app predicts whether a client will subscribe to a term deposit based on their profile and campaign data.
""")

# Load Models
@st.cache_resource
def load_models():
    models = {}
    model_names = [
        "Logistic_Regression",
        "Decision_Tree",
        "KNN",
        "Naive_Bayes",
        "Random_Forest",
        "XGBoost"
    ]
    for name in model_names:
        path = f"models/{name}.pkl"
        if os.path.exists(path):
            models[name.replace("_", " ")] = joblib.load(path)
    return models

models = load_models()

if not models:
    st.error("No models found. Please train the models first using 'train_model.py'.")
    st.stop()

# Sidebar - Model Selection
st.sidebar.header("Select Model")
selected_model_name = st.sidebar.selectbox("Choose a Classification Model", list(models.keys()))
model = models[selected_model_name]

# Main Content - Input Form
st.header("Client Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    job = st.selectbox("Job", [
        "admin.", "blue-collar", "entrepreneur", "housemaid", "management", 
        "retired", "self-employed", "services", "student", "technician", 
        "unemployed", "unknown"
    ])
    marital = st.selectbox("Marital Status", ["divorced", "married", "single"])
    education = st.selectbox("Education", ["primary", "secondary", "tertiary", "unknown"])
    default = st.selectbox("Has Credit in Default?", ["no", "yes"])

with col2:
    balance = st.number_input("Average Yearly Balance (Euros)", value=0)
    housing = st.selectbox("Housing Loan?", ["no", "yes"])
    loan = st.selectbox("Personal Loan?", ["no", "yes"])
    contact = st.selectbox("Contact Communication Type", ["cellular", "telephone", "unknown"])
    day = st.number_input("Day of Month", min_value=1, max_value=31, value=15)

with col3:
    month = st.selectbox("Last Contact Month", [
        "jan", "feb", "mar", "apr", "may", "jun", 
        "jul", "aug", "sep", "oct", "nov", "dec"
    ])
    duration = st.number_input("Last Contact Duration (seconds)", min_value=0, value=0)
    campaign = st.number_input("Number of Contacts during this Campaign", min_value=1, value=1)
    pdays = st.number_input("Days passed since last contact (-1 means not previously contacted)", value=-1)
    previous = st.number_input("Number of Contacts before this Campaign", min_value=0, value=0)
    poutcome = st.selectbox("Outcome of Previous Marketing Campaign", ["failure", "other", "success", "unknown"])

# Predict Button
if st.button("Predict Subscription"):
    # Create DataFrame for input
    input_data = pd.DataFrame({
        'age': [age],
        'job': [job],
        'marital': [marital],
        'education': [education],
        'default': [default],
        'balance': [balance],
        'housing': [housing],
        'loan': [loan],
        'contact': [contact],
        'day': [day],
        'month': [month],
        'duration': [duration],
        'campaign': [campaign],
        'pdays': [pdays],
        'previous': [previous],
        'poutcome': [poutcome]
    })
    
    # Predict
    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] if hasattr(model, "predict_proba") else None
        
        st.subheader("Prediction Result")
        if prediction == 1 or prediction == 'yes': # Check if target was label encoded to 1 or kept as string
             # Usually label encoding maps 'no'->0 'yes'->1
             # If label encoder was used on y, model returns 0/1. If not, 'no'/'yes'
             # My training script uses LabelEncoder on y. So likely 0/1.
             result_text = "YES - Client will subscribe"
             st.success(result_text)
        else:
             result_text = "NO - Client will NOT subscribe"
             st.error(result_text)
             
        if probability is not None:
            st.write(f"Probability of Subscription: {probability:.2%}")
            
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Footer
st.markdown("---")
st.markdown("Implemented for ML Assignment 2")
