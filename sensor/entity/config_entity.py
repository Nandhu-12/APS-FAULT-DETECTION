import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        try:
            #here this will create a folder wherein all the ouput of the will get saved
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception  as e:
            raise SensorException(e,sys)   


class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="aps"
            self.collection_name="sensor"

            # here we are creating our dataingestion directory
            # and inside that a folder artifact will be created and within that we will have one more folder timestamp
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir , "data_ingestion")

            #contains file location
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)

            # here dataset is a common folder where we keep train and test files
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception  as e:
            raise SensorException(e,sys)     

    # creating this function as we want to convert everything as dict
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception  as e:
            raise SensorException(e,sys)


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...