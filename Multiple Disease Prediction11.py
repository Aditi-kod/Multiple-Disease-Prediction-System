# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 13:12:17 2025

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# loading the saved models

diabetes_model = pickle.load(open('C:/Users/HP/Desktop/MDPS/trained_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/HP/Desktop/MDPS/heart_disease_model (1).sav','rb'))

#sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons = ['droplet-fill','heart-pulse'],
                           default_index = 0)
    
    #                -----DIABETES PREDICTION----   
# diabetes prediction page
if(selected == 'Diabetes Prediction'):
    # title of page
    st.title('Diabetes Prediction')
    # columns for input field
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    with col2:
        Age = st.text_input('Age of Patient')
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is suffering from Diabetes'
        else:
            diab_diagnosis = 'The person is not suffering from Diabetes'
    
    st.success(diab_diagnosis)
    
#                   ---HEART DISEASE PREDICTION----
# heart disease prediction page
if(selected == 'Heart Disease Prediction'):
    #title of page
    st.title('Heart Disease Prediction')
    # columns for input field
    
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age') 
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral(mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Number of major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    #code for prediction
    hrt_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        hrt_prediction = heart_disease_model.predict([[
    float(age), float(sex), float(cp), float(trestbps), float(chol),
    float(fbs), float(restecg), float(thalach), float(exang),
    float(oldpeak), float(slope), float(ca), float(thal)
]])

        
        if(hrt_prediction[0] == 1):
            hrt_diagnosis = 'The person is suffering from Heart Disease'
        else:
            hrt_diagnosis = 'The person is not suffering from Heart Disease'
    
    st.success(hrt_diagnosis)
    