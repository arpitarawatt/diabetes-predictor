# Diabetes-Predictor

## Overview
This project predicts whether a person is at risk of developing diabetes based on health-related input features. It uses a Machine Learning classification model deployed via a web app to deliver predictions.  
Live app: [Diabetes Predictor](https://diabetes-risk-predictor-arpitarawat.onrender.com/)

## Dataset
The dataset used for training the model is the PIMA Indians Diabetes Dataset, which is widely used for diabetes prediction tasks.

## Files
- templates/: Contains HTML files for the frontend interface of the web app.
- Diabetes.ipynb: Jupyter Notebook for data analysis, preprocessing, and model training.
- app.py: Flask application script that connects the model with the web interface.
- diabetes_logistic_regression_model.pkl: Pickled trained Logistic Regression model used for predictions.
- requirements.txt: List of dependencies required to run the project.

## Features
- Input custom health parameters to predict diabetes risk.  
- Shows if you might be diabetic or not.  
- Fast and easy deployment via web.
