import sys
import os
import numpy as np
import pandas as pd
from src.exception_handler import handle_exception
from src.utils import load_object, date_feature_extractor


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise handle_exception(e)



class CustomData:
    def __init__(  self,
        blood_pressure: int,
        diabetes_status: str,
        gender: int,
        location: str,
        pre_existing_conditions: int,
        smoking_history: str,
        vaccine_dose: int,
        age: int,
        bmi: int,
        cholesterol_level: int,
        heart_attack_date: str,
        patient_id: int,
        vaccination_date: str,
        ):

        self.blood_pressure = blood_pressure
        self.diabetes_status = diabetes_status
        self.gender = gender
        self.location = location
        self.pre_existing_conditions = pre_existing_conditions
        self.smoking_history = smoking_history
        self.vaccine_dose = vaccine_dose
        self.age = age
        self.bmi = bmi
        self.cholesterol_level = cholesterol_level
        self.heart_attack_date = heart_attack_date
        self.patient_id = patient_id
        self.vaccination_date = vaccination_date

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.age],
                "Gender": [self.gender],
                "Blood Pressure": [self.blood_pressure],
                "Diabetes Status": [self.diabetes_status],
                "Location": [self.location],
                "Pre-existing Conditions": [self.pre_existing_conditions],
                "Smoking History": [self.smoking_history],
                "Vaccine Dose": [self.vaccine_dose],
                "BMI": [self.bmi],
                "Cholesterol Level": [self.cholesterol_level],
                "Heart Attack Date": [self.heart_attack_date],
                "Patient ID": [self.patient_id],
                "Vaccination Date": [self.vaccination_date],
            }

            df = pd.DataFrame(custom_data_input_dict)
            df["Heart Attack Date"] = pd.to_datetime(df["Heart Attack Date"], errors='coerce')
            df["Vaccination Date"] = pd.to_datetime(df["Vaccination Date"], errors='coerce')

            date_feature_extractor(df, date_column="Heart Attack Date")
            date_feature_extractor(df, date_column="Vaccination Date")

            return df

        except Exception as e:
            raise handle_exception(e)
