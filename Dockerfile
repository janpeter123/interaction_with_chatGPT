#syntax=docker/dockerfile:1

#Defining Base Image
FROM python:3.11.0rc2-alpine3.16

#Defining Work Directory
WORKDIR /rest_api

#Copying Requirements file to Workdir
COPY requirements.txt requirements.txt

#Installing Requirements.txt
RUN pip3 install -r requirements.txt

#Copying local files to workdir inside container
COPY . .

#Running our Application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

