from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # variables to handle the case where we need to convert empty strings to NaN
        pre_existing_conditions = request.form.get('pre_existing_conditions')
        if pre_existing_conditions in ("", "None"):
            pre_existing_conditions = np.nan

        data = CustomData(
            blood_pressure=request.form.get('blood_pressure'),
            diabetes_status=request.form.get('diabetes_status'),
            gender=request.form.get('gender'),
            location=request.form.get('location'),
            pre_existing_conditions=pre_existing_conditions,
            smoking_history=request.form.get('smoking_history'),
            vaccine_dose=request.form.get('vaccine_dose'),
            age=int(request.form.get('age')),
            bmi=float(request.form.get('bmi')),
            cholesterol_level=int(request.form.get('cholesterol_level')),
            heart_attack_date=request.form.get('heart_attack_date'),
            patient_id=int(request.form.get('patient_id')),
            vaccination_date=request.form.get('vaccination_date')
        )
        
        print(f"Gender: {request.form.get('gender')}")
        print(f"Location: {request.form.get('location')}")
        
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        
        return render_template('home.html', results=np.round(results[0], 2))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0")