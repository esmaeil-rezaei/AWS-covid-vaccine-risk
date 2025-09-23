# import pytest
import numpy as np
from dataclasses import dataclass
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


@dataclass
class SamplePatient:
    sample_patient_dict = {
        "Age": 43,
        "Gender": "Female",
        "Blood Pressure": "Very High",
        "Diabetes Status": "Yes",
        "Location": "Washington",
        "Pre-existing Conditions": "Heart Disease",
        "Smoking History": "Yes",
        "Vaccine Dose": "2nd Dose",
        "BMI": 19.0,
        "Cholesterol Level": 350,
        "Heart Attack Date": "2021-12-16",
        "Patient ID": 392,
        "Vaccination Date": "2022-01-16",
    }


if __name__ == "__main__":
    """Test PredictPipeline with sample data"""
    sample_patient_dict = SamplePatient().sample_patient_dict
    custom_data_obj = CustomData(
        blood_pressure=sample_patient_dict["Blood Pressure"],
        diabetes_status=sample_patient_dict["Diabetes Status"],
        gender=sample_patient_dict["Gender"],
        location=sample_patient_dict["Location"],
        pre_existing_conditions=sample_patient_dict["Pre-existing Conditions"],
        smoking_history=sample_patient_dict["Smoking History"],
        vaccine_dose=sample_patient_dict["Vaccine Dose"],
        age=sample_patient_dict["Age"],
        bmi=sample_patient_dict["BMI"],
        cholesterol_level=sample_patient_dict["Cholesterol Level"],
        heart_attack_date=sample_patient_dict["Heart Attack Date"],
        patient_id=sample_patient_dict["Patient ID"],
        vaccination_date=sample_patient_dict["Vaccination Date"],
    )

    test_df = custom_data_obj.get_data_as_data_frame()
    pipeline = PredictPipeline()
    predictions = pipeline.predict(test_df)

    # Debug output in pytest (visible only if the test fails, or run with -s)
    print(predictions)

    # Assertions
    assert isinstance(predictions, (np.ndarray, list))
    assert len(predictions) > 0
