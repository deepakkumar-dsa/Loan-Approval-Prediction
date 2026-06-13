import streamlit as st
import pickle
import pandas as pd

# ---------------------------
# Load saved files
# ---------------------------
model = pickle.load(open(r"D:\Python learning\New folder (2)\loan_model.pkl", "rb"))
scaler = pickle.load(open(r"D:\Python learning\New folder (2)\scaler.pkl", "rb"))
encoders = pickle.load(open(r"D:\Python learning\New folder (2)\encoders.pkl", "rb"))

# ---------------------------
# Page Title
# ---------------------------
st.title("🏦 Loan Approval Prediction System")
st.write("Enter customer details to check loan approval status")

# ---------------------------
# User Inputs
# ---------------------------
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income_annum = st.number_input("Annual Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in months)", min_value=0)
cibil_score = st.number_input("CIBIL Score", min_value=0)
residential_assets_value = st.number_input("Residential Assets Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0)

# ---------------------------
# Prediction Button
# ---------------------------
if st.button("Predict Loan Status"):

    # Encode categorical values
    education = encoders['education'].transform([education])[0]
    self_employed = encoders['self_employed'].transform([self_employed])[0]

    # Create dataframe
    data = pd.DataFrame([{
        'no_of_dependents': no_of_dependents,
        'education': education,
        'self_employed': self_employed,
        'income_annum': income_annum,
        'loan_amount': loan_amount,
        'loan_term': loan_term,
        'cibil_score': cibil_score,
        'residential_assets_value': residential_assets_value,
        'commercial_assets_value': commercial_assets_value,
        'luxury_assets_value': luxury_assets_value,
        'bank_asset_value': bank_asset_value
    }])

    # Scale numeric columns
    num_cols = [
        'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
        'residential_assets_value', 'commercial_assets_value',
        'luxury_assets_value', 'bank_asset_value'
    ]

    data[num_cols] = scaler.transform(data[num_cols])

    # Predict
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    # Show result
    if prediction == 1:
        st.success(f"✅ Loan Approved (Confidence: {probability:.2f})")
    else:
        st.error(f"❌ Loan Rejected (Confidence: {1 - probability:.2f})")