# KP : 'kplogger_module' Imports & Utlizes logging mechanism in Python
import logging

#Create Logger with 'KPPythonApp'
logger = logging.getLogger('KPPythonApp')
logger.setLevel(logging.DEBUG)

#KP : Define KPLogger Class
class KPLogger:
    #KP : KPLogger Class Initializer/Constructor
    def __init__(self):
        self.logger = logging.getLogger("KP : KPPythonApp-PythonLogger.KPLogger");
        #File Handler : fh
        fh = logging.FileHandler('KPPythonAppLogger.log')        
        fh.setLevel(logging.DEBUG)
        #Console Handler : ch
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        #Create Formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #Add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)

    def __kplogger_log(self):
        self.logger.info("KP : KPPythonApp-PythonLogger.KPLogger")