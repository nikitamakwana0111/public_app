# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:28:35 2024

@author: BHUMI
"""

import pickle
import streamlit as st
import pyodbc
from streamlit_option_menu import option_menu


# Function to get model prediction
def predict_heart_disease(features):
    # Load the model
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    # Assuming features is a list or array
    features = np.array(features).reshape(1, -1)  # Reshape features for prediction
    prediction = heart_disease_model.predict(features)
    return prediction

# Sidebar and input fields...

# Predict heart disease
if st.button('Heart Disease Test Result'):
    # Get user inputs
    user_inputs = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    # Execute SQL query to get prediction
    conn = init_connection()  # Establish connection
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

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction'],
                           icons=['heart'],
                           default_index=0)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Execute SQL query to get prediction
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM YourTable WHERE Age = ? AND Sex = ? AND ...", (age, sex, ...))
        result = cursor.fetchone()
        cursor.close()
        
        # Process prediction
        if result[0] == 1:  # Assuming the prediction is in the first column
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
