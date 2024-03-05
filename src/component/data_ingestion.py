from bs4 import BeautifulSoup
import pandas as pd 
import os 
import sys
import numpy as np
import requests
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import re


@dataclass
class DataIngestionConfig:
    csv_file_path=os.path.join('artifacts','tmp.csv')

class Reading_server:
    def __init__(self):
        self.output_file=DataIngestionConfig()

    def innitate_reading(self,url:str):
        logging.info("enter the Data Ingestion")#wrting the logs 
        try:
            url_data=requests.get(url)
            soup=BeautifulSoup(url_data.text,'html.parser')
            logging.info("data has been read")
            regex=re.compile('.*comment.*')
            results=soup.find_all('p',{'class':regex})
            reviews=[result.text for result in results ]
            df=pd.DataFrame(np.array(reviews),columns=['review'])
            
            df.to_csv('artifacts\tmp.csv')

            logging.info("writing the data csv")
            



        except Exception as e:
            raise CustomException(e,sys)


      
