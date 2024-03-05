import logging
import os 
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"#log file ban rhi h
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #current work directory with log file  creatd above 
os.makedirs(log_path,exist_ok=True)#log path

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)
logging.basicConfig(
  filename=LOG_FILE_PATH,#file pah from above
  format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",#format defined bypyhton documentation
  level=logging.INFO, #logging.info

)


if __name__=="__main__":
    logging.info("logging has started")


