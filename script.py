# KP : Import 'sys' Commands
import sys
import math
import os

# KP : import requests #KP : Run Command : 'pip install requests' : Installs 'requests' library
import requests

# KP : Import 'print' commandcl
print(sys.version)
print(sys.executable)

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
print("KP : " + url + " Status Code : " + str(r.status_code))

# KP : Initialize Local API Requests - With Headers - http:// 200 OK Response
url = "http://kpmvcwebapis.com/api/Persons/27"
headers = {
    "content-type": "application/json",
    "accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
    "accept-Encoding": "gzip, deflate",
    "accept-language": "en-US, en; q=0.5",
    "Connection": "Keep-Alive",
}
response = requests.get(url, headers=headers)
print("KP : " + url + " Status Code : " + str(response.status_code))
print(response.text)

# KP : Initialize External API Requests
url = "https://www.cnn.com/"
response = requests.get(url)
print("KP : " + url + " Status Code : " + str(response.status_code))
# print(response.text);

