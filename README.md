### KPPythonApp

# Getting Started with Create Python App

### `py`
Run following commands to run the Python  App
Python & Microsoft MS SQL :
	Install Python Modules 
	python.exe -m pip install –upgrade pip
	py -m pip install requests 
	pip install mssql-python
	pip install pyodbc 	###KP : PYODBC Module to connect to the MSSQL Servers
	pip install python-dotenv
	pip install uvicorn  	###KP : Modules to install and host the Python WebAPIs
	pip install simplejson 	###KP : Modules to install json (JavaScript Object Notation)
	pip install pandas	
	Install Python ODBC (OpenDataBaseConnection) : pip install pyodbc
	 
	Run Script : python mssqlcon.py 
	 
	Run : python -m uvicorn mssqlconn:app --reload
	PS C:\Projects\VSCodeProjects\KPPythonApp\backend\mssqlpy> python -m uvicorn mssqlconn:app --reload
	INFO:     Will watch for changes in these directories: ['C:\\Projects\\VSCodeProjects\\KPPythonApp\\backend\\mssqlpy']
	INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
	 
	API Call on Postman : http://localhost:8000/all
	![alt text](Literature/KPReactJSWebApp.png)


## Learn More Python Literature & Documentation

	https://docs.python.org/3/index.html 
	Important reason to include ‘__init__.py’ file is to make the python modules inside sub-directories visible …
	https://stackoverflow.com/questions/1260792/import-a-file-from-a-subdirectory
	https://www.w3schools.com/python/python_mysql_getstarted.asp

