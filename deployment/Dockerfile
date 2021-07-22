FROM python:3.8

LABEL maintainer="armyost@naver.com"

COPY . /app/server

WORKDIR /app/server

EXPOSE 80

RUN apt-get update

RUN apt-get install -y python-flask

ENTRYPOINT ["python", "run.py"]

