#KP : Import 'sys' Commands
import sys

#KP : import requests #KP : Run Command : 'pip install requests' : Installs 'requests' library
import requests

#KP : Import 'print' command
print(sys.version)
print(sys.executable)

#KP : define 'greet()' 
def greet(who_to_greet):
    greeting = 'KP : Hello, {}'.format(who_to_greet)
    return greeting

#KP : Print 'greet()'
print(greet('World'))
print(greet('Kailash'))

#KP : Initialize Local API Requests
url = "http://kpmvcwebapis.com/api/Persons/27"
r = requests.get(url)
print("KP : " + url + " Status Code : " + str(r.status_code))

#KP : Initialize External API Requests
url = "https://www.cnn.com/"
r = requests.get(url)
print("KP : " + url + " Status Code : " + str(r.status_code))


