
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load model
with open('Sasithon_model.pkl', 'rb') as file:
    model, label_encoder_gender, label_encoder_hypertension, label_encoder_ever_married, \
    label_encoder_work_type, label_encoder_Residence_type, label_encoder_smoking_status = pickle.load(file)

# Define Streamlit app
st.image('stroketypes.png', width=400)
st.title('Brain Stroke Prediction')
st.subheader('Sasithon Dontree')

# Mapping dictionaries for categorical variables
gender_map = {'Male': 1, 'Female': 0}
hypertension_map = {'No': 0, 'Yes': 1}
heart_disease_map = {'No': 0, 'Yes': 1}
ever_married_map = {'No': 0, 'Yes': 1}
work_type_map = {'Private': 1, 'Self-employed': 2, 'Govt_job': 0,'children':3}
Residence_type_map = {'Urban': 1, 'Rural': 0}
smoking_status_map = {'Formerly Smoked':1, 'Never Smoked': 2, 'Smokes': 3, 'Unknown': 0}

# Get user input for each variable
gender = st.radio('Gender:', ['Male', 'Female'])
age = st.number_input('Age:', min_value=1, max_value=90, step=1)
hypertension = st.radio('Hypertension:', ['No', 'Yes'])
heart_disease = st.radio('Heart Disease:', ['No', 'Yes'])
ever_married = st.radio('Ever Married:', ['No', 'Yes'])
work_type = st.selectbox('Work Type:', ['Private', 'Self-employed', 'Govt_job', 'Never_worked'])
Residence_type = st.radio('Residence Type:', ['Urban', 'Rural'])
avg_glucose_level = st.number_input('Average Glucose Level:', min_value=0.0, max_value=300.0, step=0.1)
bmi = st.number_input('BMI:', min_value=0.0, max_value=100.0, step=0.1)
smoking_status = st.radio('Smoking Status:', ['Formerly Smoked', 'Never Smoked', 'Smokes', 'Unknown'])

# Button to submit the form
if st.button('Submit'):
    # Encode categorical variables
    gender_encoded = gender_map[gender]
    hypertension_encoded = hypertension_map[hypertension]
    heart_disease_encoded = heart_disease_map[heart_disease]
    ever_married_encoded = ever_married_map[ever_married]
    work_type_encoded = work_type_map[work_type]
    Residence_type_encoded = Residence_type_map[Residence_type]
    smoking_status_encoded = smoking_status_map[smoking_status]

    # Create DataFrame with user input
    new_data = pd.DataFrame({
        'gender': [gender_encoded],
        'age': [age],
        'hypertension': [hypertension_encoded],
        'heart_disease': [heart_disease_encoded],
        'ever_married': [ever_married_encoded],
        'work_type': [work_type_encoded],
        'Residence_type': [Residence_type_encoded],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'smoking_status': [smoking_status_encoded]
    })

    # Make prediction
    prediction = model.predict(new_data)

    # Display prediction
    st.subheader('Brain Stroke Prediction')
    if prediction[0] == 1:
        st.write('<span style="color:red; font-weight:bold;">You are at risk of having a stroke.</span>', unsafe_allow_html=True)
    else:
        st.write('<span style="color:green; font-weight:bold;">You are not at risk of having a stroke.</span>', unsafe_allow_html=True)
