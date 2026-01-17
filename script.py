# KP : Import 'sys' Commands
# KP : Import python Logger
import logging
import math
import os
import sys

# KP : Import requests #KP : Run Command : 'pip install requests' : Installs 'requests' library
import requests

# KP : Import Python Logger Modules
import kppylogs.auxiliary_module
import kppylogs.kplogger_module

# KP : Import backend SQL Connectors
import backend.mysqlpy
import backend.mysqlpy.mysqlconn

# KP : Import 'print' commandcl
print(sys.version)
print(sys.executable)

#Create Logger with 'Spam_Application'
logger = logging.getLogger('kpPythonLogger_Spam_App')
logger.setLevel(logging.DEBUG)

# KP : Print & Logging
logger.info('KP : kpPythonLogger : Creating an instance of auxillary_module.Auxillary')
print('KP : kpPythonLogger : Creating an instance of auxillary_module.Auxillary')
a = kppylogs.auxiliary_module.Auxiliary()
kpl = kppylogs.kplogger_module.KPLogger()

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
    kppylogs.kplogger_module.info()
else :
    kppylogs.kplogger_module.error()



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
    kppylogs.kplogger_module.info()
else :
    kppylogs.kplogger_module.error()


# KP : Initialize External API Requests
url = "https://www.cnn.com/"
response = requests.get(url)
if (response.ok) :
    respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok));
    kppylogs.kplogger_module.info()
else :
    respString = ("KP : " + url + " Status Code : " + str(response.status_code) + " Response OK : " + str(response.ok));
    kppylogs.kplogger_module.error()

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
    kppylogs.kplogger_module.info()
    kppylogs.auxiliary_module.some_function()
    a.do_something()
  

print(respString)
# print(response.text);



# ### KP : Is Python good for front end??
# Python is generally not the standard or primary choice for web front-end development. 
# The foundational languages for building user interfaces that run in a web browser are HTML, CSS, 
# and JavaScript (or TypeScript). 
# Python's strength lies in back-end development 
# (server-side logic, databases, data analysis, machine learning). 
# However, there are ways it can be used for front-end tasks, 
# which often involve using specialized tools to work around the browser's native support for JavaScript. 

# Why Python is Not Standard for Front-End?
# Browser Compatibility: Web browsers natively understand and execute only HTML, CSS, and JavaScript. 
# They do not have a built-in Python interpreter.
# Ecosystem & Tools: The vast majority of front-end tools, libraries, and frameworks 
# (like React, Angular, and Vue.js) are built within the JavaScript ecosystem.
# Industry Standard: For a professional web development career, proficiency in JavaScript 
# and its related technologies is essential as it is the dominant industry standard for client-side programming. 

# How Python Can Be Used for Front-End
# While not conventional, several tools and approaches allow Python to play a role in front-end development: 
# Transpilers/Compilers: Tools like Brython and Transcrypt allow you to write Python code that is then converted 
# ("transpiled") into JavaScript so it can run in the browser.
# WebAssembly (WASM): Technologies like PyScript enable Python to run directly in the browser using WebAssembly, 
# opening up more possibilities for pure-Python web applications.
# Full-Stack Frameworks (Pure Python): Frameworks such as Anvil and Reflex allow developers to build entire 
# web applications (both front-end and back-end) using only Python by abstracting away the underlying HTML, CSS, 
# and JavaScript.
# Server-Side Rendering: Back-end frameworks like Django and Flask use template engines (like Jinja)
# to dynamically generate HTML content on the server before sending it to the browser.
# Data-Focused Apps: Libraries such as Streamlit and Plotly Dash are excellent for creating interactive, 
# data-focused web applications and dashboards purely in Python, primarily used in data science contexts. 

# Conclusion
# For traditional, general-purpose web front-end development, Python is not the ideal choice. 
# You should learn HTML, CSS, and JavaScript. 
# However, if your goal is to build data science applications, internal tools, or if you prefer 
# a unified pure-Python full-stack approach, there are viable and increasingly sophisticated 
# Python-based solutions available. 