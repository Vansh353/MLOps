import os
import sys
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error
from urllib.parse import urlparse
import mlflow
import pandas as pd
import mlflow.sklearn
import numpy as np
import pickle
from src.exception.exception import customexception
from src.utils.utils import load_object
from src.logger.logging import logging
from dataclasses import dataclass
@dataclass
class ModelEvaluationConfig:
    """
    This class will be used to store all the configuration for data injestion
    """
class ModelEvaluationC:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        """
        This function will be used to initiate the data injestion process
        """
        try:
            logging.info("Initiating data injestion process")
            # Read the data
            data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/heart_disease.csv")
            logging.info("Data injested successfully")
            return data
        except Exception as e:
                logging.info()
                raise customexception(e,sys)