from flask import Flask, render_template, request, jsonify
from utils import Stroke_prediction

stroke_pp = Stroke_prediction()

app = Flask(__name__,template_folder='template')

@app.route('/')
def hello():
    print("hello flask")
    #return 'hello sanket'
    return render_template('index.html')

@app.route('/stroke_predict', methods = ['POST','GET'])
def predict_sales_price():
    if request.method == "POST":
        user_data = request.form
        gender = eval(user_data['gender'])
        age = eval(user_data['age'])
        hypertension = eval(user_data['hypertension'])
        heart_disease = eval(user_data['heart_disease'])
        ever_married = eval(user_data['ever_married'])
        Residence_type = eval(user_data['Residence_type'])
        avg_glucose_level = eval(user_data['avg_glucose_level'])
        bmi = eval(user_data['bmi'])
        work_type_index = eval(user_data['work_type_index'])
        smoking_status = eval(user_data['smoking_status'])
        
        
        print('gender','age','hypertension','heart_disease','ever_married','Residence_type','avg_glucose_level','bmi','work_type_index','smoking_status',gender, age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,work_type_index,smoking_status)
        stroke_predict = stroke_pp.price_pred(gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,work_type_index,smoking_status)
        
        #return jsonify({"Message": f"Predicted sales price is {Sales_price} $"})
        return render_template('index.html',stroke=stroke_predict)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5004)
        