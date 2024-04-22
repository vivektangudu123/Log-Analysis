import logging 
import time 
import random 

logging.basicConfig(level=logging.DEBUG, filename='logs.log') 
logger = logging.getLogger(__name__) 
formats = { 
    logging.INFO: "INFO message", 
    logging.DEBUG: "DEBUG message", 
    logging.ERROR: "ERROR message",
    logging.CRITICAL: "Critical message",
    logging.FATAL: "FATAL message",
} 
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR,logging.CRITICAL,logging.FATAL] 
while True: 
    try: 
        log_level = random.choice(log_levels) 
        log_message = formats[log_level] 
        logger.log(log_level, log_message)
        
        time.sleep(1) 
    except KeyboardInterrupt: 
        print("\nLogging interrupted. Exiting.") 
        break
