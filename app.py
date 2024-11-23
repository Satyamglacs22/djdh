import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('diabetes_model.pkl', 'rb'))

#  app title
st.title('Diabetes Prediction')

# app description
st.write("""
This is a Simple Web app to Predict whether a Person has diabetes or not.To Predict,
Please input the required values and click on the 'Predict' Button.
""")

# Function to make predictions
def predict_diabetes(features):
    return model.predict([features])

# User input for the prediction
age = st.number_input('Age', min_value=10, max_value=100, step=1)
bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1)
pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1)
glucose = st.number_input('Glucose', min_value=0, max_value=200, step=1)
blood_pressure = st.number_input('Blood Pressure', min_value=20, max_value=200, step=1)
skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1)
insulin = st.number_input('Insulin', min_value=0, max_value=900, step=1)

dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01)


# Prediction button
if st.button('Predict'):
    user_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    prediction = predict_diabetes(user_data)
    if prediction[0] == 1:
        st.write('The model predicts that you have diabetes.')
    else:
        st.write('The model predicts that you do not have diabetes.')
