# Bank Marketing Campaign Prediction - ML Assignment 2

## Project Overview
This project implements multiple classification models to predict whether a client will subscribe to a term deposit based on direct marketing campaign data from a Portuguese banking institution.

## Dataset Information
- **Source**: UCI Machine Learning Repository - Bank Marketing Dataset
- **Samples**: 45,211 instances
- **Features**: 17 input variables (16 features + 1 target)
- **Target Variable**: `y` (has the client subscribed to a term deposit? yes/no)

### Features
**Categorical Variables:**
- `job`: Type of job (admin., blue-collar, entrepreneur, etc.)
- `marital`: Marital status (divorced, married, single)
- `education`: Education level (primary, secondary, tertiary, unknown)
- `default`: Has credit in default? (yes/no)
- `housing`: Has housing loan? (yes/no)
- `loan`: Has personal loan? (yes/no)
- `contact`: Contact communication type (cellular, telephone, unknown)
- `month`: Last contact month of year
- `poutcome`: Outcome of the previous marketing campaign

**Numerical Variables:**
- `age`: Client's age
- `balance`: Average yearly balance in euros
- `day`: Last contact day of the month
- `duration`: Last contact duration in seconds
- `campaign`: Number of contacts performed during this campaign
- `pdays`: Number of days since the client was last contacted (-1 means not previously contacted)
- `previous`: Number of contacts performed before this campaign

## Models Implemented

Six different classification algorithms were implemented and evaluated:

1. **Logistic Regression**
2. **Decision Tree Classifier**
3. **K-Nearest Neighbors (KNN)**
4. **Naive Bayes (Gaussian)**
5. **Random Forest**
6. **XGBoost**

## Model Performance

| Model | Accuracy | AUC Score | Precision | Recall | F1 Score | MCC |
|-------|----------|-----------|-----------|---------|----------|-----|
| **XGBoost** | **90.88%** | **0.9313** | **0.6557** | **0.5133** | **0.5758** | **0.5305** |
| Random Forest | 90.56% | 0.9272 | 0.6782 | 0.4134 | 0.5137 | 0.4823 |
| Logistic Regression | 89.87% | 0.9046 | 0.6532 | 0.3419 | 0.4489 | 0.4245 |
| KNN | 89.85% | 0.8520 | 0.6329 | 0.3776 | 0.4730 | 0.4380 |
| Decision Tree | 87.31% | 0.7080 | 0.4747 | 0.4904 | 0.4824 | 0.4102 |
| Naive Bayes | 84.58% | 0.8099 | 0.3937 | 0.5142 | 0.4459 | 0.3626 |

**Best Performing Model**: XGBoost with an AUC score of 0.9313 and accuracy of 90.88%

## Project Structure
```
ML_Assignment_2/
│
├── app.py                      # Streamlit web application
├── train_model.py              # Model training script
├── requirements.txt            # Python dependencies
├── bank-full.csv              # Dataset
├── model_results.csv          # Model evaluation results
├── README.md                  # This file
│
└── models/                    # Trained models directory
    ├── Logistic_Regression.pkl
    ├── Decision_Tree.pkl
    ├── KNN.pkl
    ├── Naive_Bayes.pkl
    ├── Random_Forest.pkl
    ├── XGBoost.pkl
    └── label_encoder.pkl
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Installation

1. Clone or download the repository

2. Navigate to the project directory:
```bash
cd ML_Assignment_2
```

3. Create a virtual environment (recommended):
```bash
python -m venv venv
```

4. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

5. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Training the Models

To train all six models:
```bash
python train_model.py
```

This will:
- Load and preprocess the dataset
- Train all 6 classification models
- Evaluate each model using multiple metrics
- Save trained models in the `models/` directory
- Generate `model_results.csv` with evaluation metrics

### Running the Streamlit App

To launch the interactive web application:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

### Using the Web App

1. Select a classification model from the sidebar
2. Fill in the client information form with relevant details
3. Click "Predict Subscription" to get the prediction
4. The app will display whether the client is likely to subscribe and the probability

## Deployment on Streamlit Community Cloud

### Steps to Deploy:

1. **Upload to GitHub**:
   - Create a new GitHub repository
   - Push all project files (excluding `venv/` folder)
   - Ensure `requirements.txt`, `app.py`, and model files are included

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch, and `app.py` as the main file
   - Click "Deploy"

3. **Share the Link**:
   - Once deployed, you'll receive a public URL (e.g., `https://your-app.streamlit.app`)
   - Share this link for evaluation

## Evaluation Metrics Explained

- **Accuracy**: Overall correctness of predictions
- **AUC (Area Under ROC Curve)**: Measure of the model's ability to distinguish between classes
- **Precision**: Proportion of true positive predictions among all positive predictions
- **Recall**: Proportion of true positive predictions among all actual positives
- **F1 Score**: Harmonic mean of precision and recall
- **MCC (Matthews Correlation Coefficient)**: Balanced measure considering all confusion matrix categories

## Key Findings

1. **XGBoost** achieved the best overall performance with the highest AUC (0.9313) and F1 Score (0.5758)
2. **Random Forest** also performed well with an AUC of 0.9272
3. **Ensemble methods** (Random Forest, XGBoost) significantly outperformed individual classifiers
4. The dataset shows class imbalance (fewer clients subscribe), which affects precision and recall

## Technologies Used

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning algorithms and preprocessing
- **XGBoost**: Gradient boosting implementation
- **Streamlit**: Web application framework
- **matplotlib & seaborn**: Data visualization
- **joblib**: Model serialization

## Assignment Requirements Completed

✅ Dataset Selection: Bank Marketing dataset (45,211 samples, 17 features)  
✅ Model Implementation: All 6 required models implemented  
✅ Evaluation Metrics: All 6 metrics calculated (Accuracy, AUC, Precision, Recall, F1, MCC)  
✅ Streamlit App: Interactive web application developed  
✅ GitHub Repository: Complete source code with README  
✅ Deployment Ready: Instructions for Streamlit Community Cloud deployment  
✅ BITS Lab Execution: Completed (screenshot to be uploaded separately)

## Author
**Uma Mahesh**  
M.Tech (AIML/DSE)  
BITS Pilani Work Integrated Learning Programme

## Assignment Details
- **Course**: Machine Learning
- **Assignment**: Assignment 2
- **Submission Deadline**: 15-Feb-2026
- **Total Marks**: 15

## License
This project is created for educational purposes as part of the ML course curriculum.
