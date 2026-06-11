# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:18:53 2026

@author: ASUS
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os






# Get the directory where your script is currently located
working_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths relative to your script's location
# Files are in the root directory, so we don't need 'saved_models' in the path
diabetes_model = pickle.load(open(os.path.join(working_dir, 'diabetes_trained_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(working_dir, 'heart_disease.sav'), 'rb'))
parkinsons_model = pickle.load(open(os.path.join(working_dir, 'parkinson_model.sav'), 'rb'))
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System" , 
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Disease Prediction'],
                           
                           icons = ['activity' , 'heart' ,'person'],
                           
                           default_index = 0
                           
                           )
    
# Diabetes Prediction Page
if(selected == "Diabetes Prediction"):  # This is of the sidebar 
    #page title
    st.title('Diabetes Prediction') # This is the main page
    
    
    
    
    
    # columns for input field
    col1 , col2 , col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    
    with col2:
        Glucose = st.text_input('Your glucose level')
        
    with col3:
        BloodPressure = st.text_input('Your Blood Pressure')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Levels')
    
    
    with col2:
        Insulin = st.text_input('Your Insulin Levels')
        
    with col3:
        BMI = st.text_input('Your BMI')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('dpf value')
        
    with col2:
        Age = st.text_input('Your age')
    
    
    
    
    
    
    
    
   
   
    
    
   
    
    
    #code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if st.button("Diabetes Test Prediction"):
        diab_prediction = diabetes_model.predict([[Pregnancies , Glucose , BloodPressure , SkinThickness , Insulin , BMI , DiabetesPedigreeFunction , Age]])
        
        if(diab_prediction[0] == 0):
            diab_diagnosis = 'The person is non diabetic'
        else:
            diab_diagnosis = 'The perosn is diabetic'
    st.success(diab_diagnosis)
# Parkinsons Prediction
if(selected == "Parkinson Disease Prediction"):
    
    # page title
    st.title('Parkinson Disease Prediction')
    Age = st.text_input('Your age')
    Gender = st.text_input('Your gender')
    Ethnicity = st.text_input('Your ethnicity')
    EducationLevel = st.text_input('Your education')
    BMI = st.text_input('Your bmi')
    Smoking = st.text_input('do you smoke')
    AlcoholConsumption = st.text_input('do you consume alcohol')
    PhysicalActivity = st.text_input('do you exercise')
    DietQuality = st.text_input('Your diet')
    SleepQuality = st.text_input('Your sleep quality')
    FamilyHistoryParkinsons = st.text_input('Your family history')
    TraumaticBrainInjury = st.text_input('any traumatic injury')
    Hypertension = st.text_input('hypertension')
    Diabetes = st.text_input(' did you have diabetes')
    Depression = st.text_input('did you have depression')
    Stroke = st.text_input('Your stroke')
    SystolicBP = st.text_input('Your systolic BP')
    DiastolicBP = st.text_input('Your diastolic BP')
    CholesterolTotal = st.text_input('Your Cholestrol')
    CholesterolLDL = st.text_input('Your Cholestrol LDL')
    CholesterolHDL = st.text_input('Your Cholestrol HDL')
    CholesterolTriglycerides = st.text_input('Your Cholestrol Triglycerides')
    UPDRS = st.text_input('Your UPDRS')
    MoCA = st.text_input('Your MoCA')
    FunctionalAssessment = st.text_input('Your Functional Assesment')
    Tremor = st.text_input('Your Tremor')
    Rigidity = st.text_input('Your Rigidity')
    Bradykinesia = st.text_input('Your Bradykinesia')
    PosturalInstability = st.text_input('any Postural Instability')
    SpeechProblems = st.text_input('speech problems')
    SleepDisorders = st.text_input('sleep disorders')
    Constipation = st.text_input('constipation')
   
    park_diagnosis = ''
    
    if st.button('Parkinsons disease prediction'):
        park_prediction = parkinson_model.predict([[Age , Gender , Ethnicity , EducationLevel , BMI ,  Smoking , AlcoholConsumption , PhysicalActivity , DietQuality , SleepQuality , FamilyHistoryParkinsons , TraumaticBrainInjury ,  Hypertension , Diabetes , Depression , Stroke , SystolicBP , DiastolicBP , CholesterolTotal , CholesterolLDL ,  CholesterolHDL , UPDRS , MoCA , FunctionalAssessment,Tremor , Rigidity, Bradykinesia , PosturalInstability ,  SpeechProblems ,  SleepDisorders , Constipation  ]])
        
        if(park_prediction[0] == 0):
            park_diagnosis = 'The person is not suffering from parkinson disease'
        else:
            park_diagnosis = 'The person is suffering from parkinson disease'
            
    st.success(park_diagnosis)
# Heart Disease Prediction 
if(selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction ')
    Age = st.text_input('Your age')
    sex = st.text_input('Your Sex')
    cp = st.text_input('Your cp')
    trestbps = st.text_input('Your trestbps')
    chol = st.text_input('chol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('old peak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    
    heart_diagnosis = ''
    
    if st.button( "Heart disease Prediction"):
        heart_prediction =heart_model.predict([[Age , sex , cp , trestbps , chol , fbs , restecg , thalach , exang , oldpeak , slope , ca , thal]])
        
        if(heart_prediction[0] == 0):
            heart_diagnosis = 'The person is not suffering from any heart disease'
        else :
            heart_diagnosis = 'The person is suffering from heart disease'
    st.success(heart_diagnosis)
        
    