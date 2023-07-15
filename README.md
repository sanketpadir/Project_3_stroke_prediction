# Project_3_stroke_prediction
Welcome to the project! This repository contains an application that predicts the likelihood of stroke using a given dataset. The application utilizes several algorithms and evaluates them to select the best model, which is then saved as a pickle file for production use.

# About Data set info:
According to the World Health Organization (WHO), stroke is the second leading cause of death globally, accounting for approximately 11% of total deaths. This dataset aims to predict whether a patient is likely to have a stroke based on various input parameters, including gender, age, presence of hypertension, heart disease, marriage status, work type, residence type, average glucose level, body mass index (BMI), smoking status, and stroke occurrence. Each row in the dataset provides relevant information about a patient.

# The dataset includes the following features:

1) id: unique identifier
   
2) gender: "Male", "Female" or "Other"
   
3) age: age of the patient
   
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
   
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
    
6) ever_married: "No" or "Yes"
    
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
    
8) Residence_type: "Rural" or "Urban"
    
9) avg_glucose_level: average glucose level in blood
    
10) bmi: body mass index
    
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
    
12) stroke: 1 if the patient had a stroke or 0 if not
    

The independent variables considered for predicting stroke are 'age', 'gender', 'BMI', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'residence_type', 'avg_glucose_level', and 'smoking_status'. The dependent variable is 'stroke'. The prediction of stroke occurrence depends on these independent variables, and each variable directly impacts the likelihood of stroke.

# libraries and tools
The code is written in Python and utilizes the following libraries and tools:

numpy

pandas

scikit-learn (sklearn)

matplotlib

seaborn

pickle

# installation
To set up the necessary dependencies, run the following command to install them:

pip install -r requirements.txt

# usage
To run the project, follow these steps:

1.Open the command prompt and execute the following command: python interface.py

2.Copy the URL displayed in the command prompt and paste it into your web browser. This will open the frontend of the application.

3.Enter your information according to the provided parameters and retrieve the predicted likelihood of stroke.

Enjoy using the application!

Please let me know if you have any further questions or if there's anything else I can assist you with.
