
import os
import numpy as np 
import requests
import pandas as pd
from src.exception_handler import handle_exception
from src.logger import logging
import pickle
from sklearn.metrics import r2_score, accuracy_score
from sklearn.model_selection import GridSearchCV




# def fetch_kaggle_as_dataframe(kaggle_url: str, file_name: str) -> pd.DataFrame:
#     """
#     Fetch Kaggle csv data and convert it into a pandas DataFrame.
#     """
#     try:
#         path = kagglehub.dataset_download(kaggle_url)
#         csv_path = os.path.join(path, file_name)
#         df = pd.read_csv(csv_path)

#         return df

#     except Exception as e:
#         raise handle_exception(e)
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise handle_exception(e)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, param, problem_type='classification'):
    """
    Evaluate multiple models using GridSearchCV and return their scores.
    
    problem_type: 'regression' or 'classification'
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            para = param[model_name]

            if problem_type == 'classification':
                scoring = 'accuracy'
            else:
                scoring = 'r2'

            gs = GridSearchCV(model, para, cv=3, scoring=scoring)
            gs.fit(X_train, y_train)

            # Set the best parameters found by GridSearch
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            if problem_type == 'classification':
                score = accuracy_score(y_test, y_test_pred)
            else:
                score = r2_score(y_test, y_test_pred)

            report[model_name] = score

        return report

    except Exception as e:
        raise handle_exception(e)
    

    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise handle_exception(e)

def binary_encoder(df, target):
    try:
        df[target] = df[target].astype(int)
        return df
    except Exception as e:
        raise handle_exception(e)
    

def date_feature_extractor(df, date_column):
    try:
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        df[f'{date_column}_year'] = df[date_column].dt.year
        df[f'{date_column}_month'] = df[date_column].dt.month
        df[f'{date_column}_day'] = df[date_column].dt.day
        df[f'{date_column}_day_of_week'] = df[date_column].dt.dayofweek  # Monday=0, Sunday=6
        df[f'{date_column}_quarter'] = df[date_column].dt.quarter  # 1, 2, 3, or 4
        df[f'{date_column}_is_weekend'] = (df[date_column].dt.weekday >= 5).astype(int)  # 1 for weekend, 0 for weekdays
        df.drop(columns=[date_column], inplace=True)
        return df
    except Exception as e:
        raise handle_exception(e)
