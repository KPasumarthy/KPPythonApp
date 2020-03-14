# KP : Import 'sys' Commands
# KP : Import python Logger
import logging
import math
import os
import sys

# KP : Import requests #KP : Run Command : 'pip install requests' : Installs 'requests' library
import requests

import auxiliary_module
import kplogger_module

# KP : Import 'print' commandcl
print(sys.version)
print(sys.executable)

#Create Logger with 'Spam_Application'
logger = logging.getLogger('kpPythonLogger_Spam_App')
logger.setLevel(logging.DEBUG)

# KP : Print & Logging
logger.info('KP : kpPythonLogger : Creating an instance of auxillary_module.Auxillary')
print('KP : kpPythonLogger : Creating an instance of auxillary_module.Auxillary')
a = auxiliary_module.Auxiliary()
kpl = kplogger_module.KPLogger()

# KP : define 'greet()'
def greet(who_to_greet):
    # test = "Test"
    greeting = "KP : Hello, {}".format(who_to_greet)
    return greeting

# KP : Print 'greet()'
print(greet("World"))
print(greet("Kailash"))

# KP : Get Input and Print
name = input("Your Name ? >> ")
print("KP : Hello, ", name)

# KP : Initialize Local API Requests - With OUT Headers - http:// 500 Error Response
url = "http://kpmvcwebapis.com/api/Persons/27"
r = requests.get(url)
print("KP : " + url + " Status Code : " + str(r.status_code)  + " Response OK : " + str(r.ok))
if(r.ok) :
    kplogger_module.info()
else :
    kplogger_module.error()



# KP : Initialize Local API Requests - With Headers - http:// 200 OK Response
url = "http://kpmvcwebapis.com/api/Persons/27"
headers = {
    "content-type": "application/json",
    "accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
    "accept-Encoding": "gzip, deflate",
    "accept-language": "en-US, en; q=0.5",
    "connection": "keep-alive",
}
response = requests.get(url, headers=headers)
respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok))
print(respString)
print(response.text)
if(response.ok) :
    kplogger_module.info()
else :
    kplogger_module.error()


# KP : Initialize External API Requests
url = "https://www.cnn.com/"
response = requests.get(url)
if (response.ok) :
    respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok));
    kplogger_module.info()
else :
    respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok));
    kplogger_module.error()

print(respString)
# print(response.text);


def greet(who_to_greet):
    # test = "Test"
    greeting = "KP : Hello, {}".format(who_to_greet)
    return greeting

# KP : Print 'greet()'
print(greet("World"))
print(greet("Kailash"))

# KP : Get Input and Print
name = input("Your Name ? >> ")
print("KP : Hello, ", name)

# KP : Initialize Local API Requests - With OUT Headers - http:// 500 Error Response
url = "http://kpmvcwebapis.com/api/Persons/27"
r = requests.get(url)
print("KP : " + url + " Status Code : " + str(r.status_code)  + " Response OK : " + str(r.ok))

# KP : Initialize Local API Requests - With Headers - http:// 200 OK Response
url = "http://kpmvcwebapis.com/api/Persons/27"
headers = {
    "content-type": "application/json",
    "accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
    "accept-Encoding": "gzip, deflate",
    "accept-language": "en-US, en; q=0.5",
    "connection": "keep-alive",
}
response = requests.get(url, headers=headers)
respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok))
print(respString)
print(response.text)

# KP : Initialize External API Requests
url = "https://www.cnn.com/"
response = requests.get(url)
if(response.ok):
    respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok));
    kplogger_module.info()
    auxiliary_module.some_function()
    a.do_something()
  

print(respString)
# print(response.text);
