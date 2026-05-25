# IBM HR Attrition Analysis 🏢

## Overview
Predicting employee attrition using IBM HR Analytics dataset 
with Machine Learning.

## Key Findings
- Employees with low monthly income are 3x more likely to leave
- Overtime workers have 31% attrition vs 10.5% for non-overtime
- Lab Technicians have highest attrition rate
- Stock Option Level is the #1 factor in predicting attrition

## Tech Stack
- Python, Pandas, Scikit-learn
- SMOTE for class imbalance
- Random Forest Classifier
- Streamlit for deployment

## Model Performance
- Accuracy: 85%
- Improved minority class recall from 10% to 26% using SMOTE

## How to Run
pip install -r requirements.txt
streamlit run app.py
