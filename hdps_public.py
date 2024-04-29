# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:28:35 2024

@author: BHUMI
"""

import pickle
import streamlit as st
import pyodbc
import numpy as np
from streamlit_option_menu import option_menu

# Initialize connection function
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

# Function to get model prediction
def predict_heart_disease(features):
    # Load the model
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    # Assuming features is a list or array
    features = np.array(features).reshape(1, -1)  # Reshape features for prediction
    prediction = heart_disease_model.predict(features)
    return prediction

# Initialize connection
conn = init_connection()

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction'],
                           icons=['heart'],
                           default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age')
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.number_input('Chest Pain types')
        trestbps = st.number_input('Resting Blood Pressure')
        chol = st.number_input('Serum Cholestoral in mg/dl')
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    with col2:
        restecg = st.number_input('Resting Electrocardiographic results')
        thalach = st.number_input('Maximum Heart Rate achieved')
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
        oldpeak = st.number_input('ST depression induced by exercise')
        slope = st.number_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', [0, 1, 2])
    
    # Predict heart disease
    if st.button('Heart Disease Test Result'):
        # Convert categorical inputs to numerical
        sex = 1 if sex == 'Male' else 0
        fbs = 1 if fbs == 'Yes' else 0
        exang = 1 if exang == 'Yes' else 0
        
        # Get user inputs
        user_inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        # Execute SQL query to get prediction
        cursor = conn.cursor()
        query = "SELECT * FROM YourTable WHERE Age = ? AND Sex = ? AND ..."  # Construct your SQL query
        cursor.execute(query, user_inputs)
        result = cursor.fetchone()
        cursor.close()
        
        # Process prediction
        if result:
            heart_diagnosis = 'The person is having heart disease' if result[0] == 1 else 'The person does not have any heart disease'
        else:
            heart_diagnosis = 'Prediction not available'
        
        st.success(heart_diagnosis)
