import pandas as pd
import numpy as np
import pickle
import json
import config

class Stroke_prediction:

    def __init__(self):
        print("INIT FUNCTION")

    def load_saved_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.stroke_data = json.load(f)

    def price_pred(self,gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,work_type_index,smoking_status):
        
        self.load_saved_data()

        test_array = np.zeros(self.model.n_features_in_, int)
        test_array[0] = gender
        test_array[1] = age
        test_array[2] = hypertension
        test_array[3] = heart_disease
        test_array[4] = ever_married
        test_array[5] = Residence_type
        test_array[6] = avg_glucose_level
        test_array[7] = bmi
        test_array[work_type_index] = 1
        test_array[smoking_status] = 1
        
        test_array

        prediction = np.around(self.model.predict([test_array])[0] , 2)
        print(f" stroke Predicted   is : {prediction} $")    
        return prediction
    
if __name__ == "__main__":
    stroke_pp =Stroke_prediction() 
    
#<form action="predict_sales_price", method="POST">
