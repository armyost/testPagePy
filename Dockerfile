FROM python:3.8

LABEL maintainer="armyost@naver.com"

WORKDIR /app
COPY ./app /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python", "app.py"]

