# Random-quotes-generator-api
Api that return random quote in every request 

## Features
- return random quote with it's aithor 
- generate a report after 100 request with quots and it's displayed count

## Response format 
{"<br /> 
  "id": [quote id],"<br /> 
  "quote":[quote text],"<br /> 
  "author":[quote author]"<br /> 
}"<br /> 

## Installation

1- clone the project <br /> 
2- create vertual env with this command "py -3 -m venv .venv"<br /> 
3- run vertual env with command ".venv\scripts\activate"<br /> 
4- install all libs and 3rd parties with command  "pip install -r requirements.txt"<br /> 
5- make migrations to setup your models and database (Sqlite3) with "python manage.py makemigrations"<br /> 

## now you can run the api with
command: "python manage.py runserver"
