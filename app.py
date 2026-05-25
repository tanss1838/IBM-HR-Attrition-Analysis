import streamlit as st
import pandas as pd
import joblib

model = joblib.load('attrition_model.pkl')
columns = joblib.load('model_columns.pkl')

st.title('Employee Attrition Predictor 🏢')
st.write('Fill in employee details to predict if they will leave')

age = st.slider('Age', 18, 60, 30)
monthly_income = st.number_input('Monthly Income', 1000, 20000, 5000)
overtime = st.selectbox('OverTime', ['Yes', 'No'])
job_satisfaction = st.slider('Job Satisfaction (1-4)', 1, 4, 3)
stock_option = st.slider('Stock Option Level (0-3)', 0, 3, 1)

if st.button('Predict'):
    input_dict = dict.fromkeys(columns, 0)
    input_dict['Age'] = age
    input_dict['MonthlyIncome'] = monthly_income
    input_dict['OverTime'] = 1 if overtime == 'Yes' else 0
    input_dict['JobSatisfaction'] = job_satisfaction
    input_dict['StockOptionLevel'] = stock_option
    
    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    
    if prediction == 1:
        st.error('⚠️ Employee is likely to LEAVE')
    else:
        st.success('✅ Employee is likely to STAY')