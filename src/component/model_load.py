from transformers import AutoTokenizer ,AutoModelForSequenceClassification
import torch
from src.logger import logging
from src.exception import CustomException
import sys 


class Model_loading:
#Loading Model from hugging Face
   def __init__(self):
      try:
       logging.info("Loading Model from higging Face")
       self.tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
       self.model=AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
      except Exception as e :
         CustomException(e,sys)
   def model_trasnformation(self,dataframe): 
      try:
       logging.info("tokenization and model transformation has been started")  
       tokens=self.tokenizer.encode(dataframe,return_tensor='pt')
       result=self.model(tokens)
       return int(torch.argmax(result.logits)+1)
      except Exception as e :
        CustomException(e,sys)