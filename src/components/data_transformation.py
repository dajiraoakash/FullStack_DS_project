import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os


@dataclass
class DataTransformationConfig:
    #pkl(pickle) for saving models
    preprcessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_tranformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch', 
                'test_preparation_course'
                ]
            
            numerical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            
            )
            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent"))
                    ("one_hot_encoder", OneHotEncoder())
                    ("scaler", StandardScaler())
                ]

            )
            
            logging.info("Categorical column Standard scaling complete")
            logging.info("Categorical column encoding complete")

            preprocessor = ColumnTransformer(
                [
                ("categorical_pipeline", categorical_pipeline,categorical_columns),
                ("numerical_pipeline", numerical_pipeline, numerical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self, train_data_path,test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info("Reading Train and test data completed")

            logging.info("Obtaining Preprocessor Object")

            preprocessing_obj = get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns=["writing_score", "reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            
            





        except Exception as e:
            raise CustomException(e,sys)