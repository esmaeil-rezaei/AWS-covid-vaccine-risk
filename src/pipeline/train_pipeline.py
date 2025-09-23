import os
import sys
from src.exception_handler import handle_exception
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass
    def run_pipeline(self):
        obj = DataIngestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )

        modeltrainer=ModelTrainer()
        print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
        logging.info("Training pipeline completed")

        
if __name__ == "__main__":
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        logging.info("Error in training pipeline")
        raise handle_exception(e)