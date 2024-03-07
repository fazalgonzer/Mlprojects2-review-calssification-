import os 
import sys
from src.exception import CustomException
from src.logger import logging
from src.component.data_ingestion import DataIngestionConfig,Reading_server
from src.component.model_load import Model_loading
import pandas as pd

class predict_pipeline:
     def __init__(self,url:str) :
       logging.info("in predict Pipeline")
       self.url=url 
     def predict(self,output):
         try:
          logging.info("In predict Pipeline")
          x1=Reading_server() 
          logging.info("inside data ingestion")
          x2=x1.innitate_reading(self.url)
          logging.info("inside csv redaing ")
          df=pd.read_csv(x2)
          y=Model_loading()
          logging.info("inside model laoding py")
          df['sentiment']=df['review'].apply(lambda x:y.model_trasnformation(x[:512]))

          df.to_csv(output)
         except Exception as e:
            CustomException(e,sys)




    
        
 