FROM python:3.7-slim
MAINTAINER "Bruno Bocardo<bruno_bocardo@hotmail.com>"

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nano

ARG PROJECT_NAME=django-test

RUN mkdir /$PROJECT_NAME
WORKDIR /$PROJECT_NAME

ADD . /$PROJECT_NAME

# Install Requirements
RUN pip3 install -r /$PROJECT_NAME/requirements.txt

EXPOSE 9000

# Make it executable
RUN chmod +x deploy/init_django.sh

CMD deploy/init_django.sh
