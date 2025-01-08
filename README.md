# SmartKart
Web application to help users minimize grocery costs by comparing prices across stores and factoring in travel expenses

## Motivation
The goal of this project is to allow shoppers to buy the groceries they need at the store that gives them the lowest aggregate cost for their cart. With grocery prices forecasted to increase 5-7% (according to a study jointly authored by Dalhouse University, University of Guelph, University of Saskachewan, and the University of British Columbia), the completion of this project will allow shoppers to minimize their total spend for groceries, thereby allowing them to allocate those savings to other necessities and comforts.

## Depedencies

### Frontend
Tools/Dependencies:
- Bootstrap
- ReactJS
### Backend
- Flask
### Database
- PostgresSQL

## Installation
First and foremost, ensure you have an IDE(s)/text editor that supports JavaScript, CSS, and Python. <a href="https://code.visualstudio.com/"> Visual Studio Code</a> is a great option as it can be used to develop in these languages with the benefit of using extensions. You will also need some application that can run a command line (ex: Terminal on MacOS/Linux, PowerShell on Windows).

### Installing Python:
- Head to the <a href="https://www.python.org/downloads/">download</a> page
- Download a version of Python that is 3.7 or newer

### Installing Bootstrap:
- Head to the <a href="https://getbootstrap.com/docs/3.4/getting-started/">download</a> page
- Click on the "Download Bootstrap" button
- Unzip the download file

### Installing ReactJS:
- No installation required, just an IDE which can support ReactJS. VSCode is recommended.

### Installing Flask/Python Libraries:
- Flask/All Python Libraries are to be installed within a virtual environment
- Open a commmand line (ex: Terminal on MacOS/Linux, PowerShell on Windows). In the project directory enter the following commands:
	- <code>python3 -m venv venv</code>
	- <code>venv/bin/activate</code>
	- <code>pip install -r requirements.txt</code>

# Usage

Run 'npm install' in smartkart/ then run 'npm start' to load the web app.

Note: db is no longer being hosted on server - need to host locally.

Connect to the psql database (SQLALCHEMY_DATABASE_URI in application.py).

Username: postgres

Password: password

Address/Host: localhost

Port: 5432

Database Name: smartkart


Note: Need to supply Google Map API Key in backend/nearest_location_search_with_distance.py
and in backend/nearest_location_search.py

Run 'python3 application.py'.



