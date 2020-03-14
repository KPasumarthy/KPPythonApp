#KP : Import Python Logging
import logging

#KP : Create Python Logger with 'Spam_Application'
module_logger = logging.getLogger("KP : Python spam_application.auxiliary")

#KP : Define Auxiliary Class
class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger("KP : Spam_application.auxiliary.Auxiliary");
        self.logger.info('KP : Creating an instance of Auxiliary')
        print('KP : Creating an instance of Auxiliary')
        
    
    def do_something(self):
        self.logger.info("KP : auxillaryModule - doingSomething()")
        print("KP : auxillaryModule - doingSomething()")
        a = 1 + 1;
        self.logger.info('KP : auxillaryModule done doing something')
        print("KP : auxillaryModule - doingSomething()")

def some_function():
    module_logger.info('KP : received a call to "some_function"')
    print("KP : auxillaryModule - doingSomething()")
