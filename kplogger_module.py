# KP : 'kplogger_module' Imports & Utlizes logging mechanism in Python
import logging

#Create Logger with 'KPPythonApp'
kplogger_module = logging.getLogger('KPPythonApp')
kplogger_module.setLevel(logging.DEBUG)

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
        kplogger_module.addHandler(fh)
        kplogger_module.addHandler(ch)

    def __kplogger_log(self):
        self.logger.info("KP : KPPythonApp-PythonLogger.KPLogger")

def info():
    kplogger_module.info('KP : KPPythonApp-PythonLogger.KPLogger "info"')
    print('KP : KPPythonApp-PythonLogger.KPLogger "info"')

def debug():
    kplogger_module.debug('KP : KPPythonApp-PythonLogger.KPLogger "debug"')
    print('KP : KPPythonApp-PythonLogger.KPLogger "debug"')

def warning():
    kplogger_module.warning('KP : KPPythonApp-PythonLogger.KPLogger "warning"')
    print('KP : KPPythonApp-PythonLogger.KPLogger "warning"')

def error():
    kplogger_module.error('KP : KPPythonApp-PythonLogger.KPLogger "error"')
    print('KP : KPPythonApp-PythonLogger.KPLogger "error"')

def exception():
    kplogger_module.exception('KP : KPPythonApp-PythonLogger.KPLogger "exception"')
    print('KP : KPPythonApp-PythonLogger.KPLogger "exception"')

        