# Loan-Approval-Prediction

Project Overview

The Loan Approval Prediction System is a Machine Learning project developed to automate the loan approval process by predicting whether a loan application will be approved or rejected based on applicant financial and demographic information.

The project uses historical loan application data and Machine Learning algorithms to analyze customer profiles, assess creditworthiness, and provide accurate loan approval predictions. A user-friendly Streamlit web application was developed to allow real-time predictions for new loan applicants.

Business Problem

Financial institutions receive thousands of loan applications every day. Manual loan evaluation is time-consuming and may lead to inconsistent decisions.

The objective of this project was to build a predictive model that can:

Reduce manual effort in loan screening
Improve loan approval decision-making
Minimize financial risk
Provide instant approval predictions
Dataset Features Used

The model was trained using the following customer attributes:

Number of Dependents
Education Level
Self-Employment Status
Annual Income
Loan Amount
Loan Term
CIBIL Score
Residential Asset Value
Commercial Asset Value
Luxury Asset Value
Bank Asset Value

Target Variable:

Loan Status
Approved (1)
Rejected (0)
Data Preprocessing
Data Cleaning

Performed multiple preprocessing steps to improve data quality:

Removed unnecessary column (loan_id)
Removed duplicate records
Checked and handled missing values
Removed extra white spaces from categorical columns
Standardized categorical values
Outlier Treatment

Used the Interquartile Range (IQR) method to detect and remove outliers from:

Residential Asset Value
Commercial Asset Value

This helped improve model stability and prediction performance.

Exploratory Data Analysis (EDA)

Performed extensive EDA to understand data patterns and relationships.

Visualizations Created
Count Plots for categorical variables
Histograms for numerical features
Box Plots for outlier detection
Correlation Heatmap
Key Insights
CIBIL Score had a strong influence on loan approval.
Applicants with higher annual income had a higher probability of approval.
Asset ownership positively impacted approval decisions.
Loan amount and loan term showed moderate influence on approval status.
Feature Engineering
Label Encoding

Converted categorical variables into numerical format:

Education
Self Employed Status
Feature Scaling

Applied StandardScaler to normalize numerical features:

Income
Loan Amount
Loan Term
CIBIL Score
Asset Values

This improved model performance and convergence.

Handling Class Imbalance

Implemented SMOTE (Synthetic Minority Oversampling Technique) to balance the target classes.

Benefits:

Reduced bias toward the majority class
Improved prediction performance for minority class samples
Increased model generalization
Machine Learning Models Implemented
1. Logistic Regression
Baseline classification model
Used class balancing
Evaluated using Accuracy, ROC-AUC, and Classification Report
2. Decision Tree Classifier
Captured non-linear relationships
Configured with controlled tree depth to reduce overfitting
3. Random Forest Classifier
Ensemble learning approach
Multiple decision trees combined for better performance
Tuned using:
Maximum Depth
Minimum Samples Split
Minimum Samples Leaf
Model Evaluation

Evaluated models using:

Accuracy Score
Confusion Matrix
Classification Report
ROC-AUC Score

After comparing all models, Random Forest Classifier achieved the best overall performance and was selected as the final production model.

Model Deployment

Developed an interactive web application using Streamlit.

Application Features
User-friendly interface
Real-time loan approval prediction
Confidence score display
Automatic preprocessing of user inputs
Scalable deployment-ready architecture
Workflow
User enters applicant details.
Categorical features are encoded.
Numerical features are scaled.
Trained Random Forest model generates prediction.
Loan approval result is displayed instantly.
Technologies Used
Category	Tools
Programming	Python
Data Analysis	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-Learn
Imbalanced Data Handling	SMOTE
Model Deployment	Streamlit
Model Storage	Pickle

