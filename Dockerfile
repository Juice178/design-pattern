FROM python:3.8.7-slim-buster

RUN apt-get update
RUN apt-get install -y vim less
RUN mkdir -p opt/design-pattern/src
COPY src/ opt/design-pattern/src
RUN pip install --upgrade pip

WORKDIR opt/design-pattern
RUN pip install poetry
RUN poetry init 
RUN poetry install
