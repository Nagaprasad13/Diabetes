import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the model
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page title
st.title('Diabetes Prediction System')

# Create input fields
st.subheader('Enter Patient Information:')

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=0)
    glucose = st.number_input('Glucose Level', min_value=0, max_value=300, value=0)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, value=0)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, value=0)

with col2:
    insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, value=0)
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=0.0)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.0)
    age = st.number_input('Age', min_value=0, max_value=120, value=0)

# Create predict button
if st.button('Predict'):
    # Create input data frame
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    
    # Show prediction
    st.subheader('Prediction Result:')
    if prediction[0] == 1:
        st.error('The person is likely to have diabetes.')
    else:
        st.success('The person is not likely to have diabetes.')
    
    st.write(f'Probability of having diabetes: {probability:.2%}')