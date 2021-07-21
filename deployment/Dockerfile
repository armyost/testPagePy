FROM python:3.8

LABEL maintainer="armyost@naver.com"

COPY . /app/server

WORKDIR /app/server

EXPOSE 80

RUN pip3 install -r ./deployment/requirements.txt 

ENTRYPOINT ["python", "run.py"]

