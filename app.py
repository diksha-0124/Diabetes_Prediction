import streamlit as st
import pickle
import numpy as np

# Load your trained model (make sure to export 'model.pkl' from your Colab)
# model = pickle.load(open('diabetes_model.pkl', 'rb'))

st.set_page_config(page_title="Diabetes Predictor", layout="centered")

st.title("🩺 Diabetes Prediction System")
st.markdown("Enter the patient's health metrics below to predict the risk of diabetes.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)

with col2:
    insulin = st.number_input("Insulin Level", min_value=0)
    bmi = st.number_input("BMI (e.g. 24.5)", min_value=0.0, format="%.1f")
    pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age",  min_value=1, step=1)

if st.button("Predict Results", use_container_width=True):
    # Prepare data for prediction
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]])
    
    # prediction = model.predict(features)
    # Placeholder result logic
    prediction = [0] 

    if prediction[0] == 1:
        st.error("### Result: High Risk of Diabetes")
    else:
        st.success("### Result: Low Risk of Diabetes")