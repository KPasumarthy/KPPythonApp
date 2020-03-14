# KP : Import python Logger
import logging
#import auxiliaryModule
import auxiliary_module

#Create Logger with 'Spam_Application'
logger = logging.getLogger('kpPythonLogger_Spam_App')
logger.setLevel(logging.DEBUG)

#Create file Handler which logs even debug messages
fh = logging.FileHandler('kpSpam.log')
fh.setLevel(logging.DEBUG)

#Create console handler with a higher log-level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#Create Formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('KP : kpPythonLogger : Creating an instance of auxillary_module.Auxillary')
print('KP : kpPythonLogger : Creating an instance of auxillary_module.Auxillary')
a = auxiliary_module.Auxiliary()
logger.info('KP : kpPythonLogger : Created an instance of auxiliary_module.Auxiliary')
print('KP : kpPythonLogger : Created an instance of auxiliary_module.Auxiliary')
logger.info('KP : kpPythonLogger : Calling auxiliary_module.Auxiliary.do_something')
print('KP : kpPythonLogger : Calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('KP : kpPythonLogger : finished auxiliary_module.Auxiliary.do_something')
print('KP : kpPythonLogger : finished auxiliary_module.Auxiliary.do_something')
logger.info('KP : kpPythonLogger : calling auxiliary_module.some_function()')
print('KP : kpPythonLogger : calling auxiliary_module.some_function()')
auxiliary_module.some_function()
logger.info('KP : kpPythonLogger : done with auxiliary_module.some_function()')
print('KP : kpPythonLogger : done with auxiliary_module.some_function()')
