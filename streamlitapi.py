import streamlit as st

# Title
st.title("Patient Readmission Risk Predictor")

# Input fields
name = st.text_input("Enter Patient's Name")
age = st.number_input("Enter Age", min_value=0, max_value=120, step=1)
diagnosis = st.selectbox("Select Diagnosis", ["Diabetes", "Cough", "Heart Disease", "Other"])
previous_admissions = st.number_input("Number of Previous Admissions", min_value=0, step=1)

# Predict risk
if st.button("Check Risk Level"):
    if previous_admissions > 2 or age >= 48:
        risk_level = "High Risk"
    else:
        risk_level = "Low Risk"

    # Display Results
    st.write(f"### Patient: {name}")
    st.write(f"Age: {age}")
    st.write(f"Diagnosis: {diagnosis}")
    st.write(f"Previous Admissions: {previous_admissions}")
    st.write(f"## Risk Level: {risk_level}")