FROM python:3.8-alpine
RUN apk update && apk add postgresql-dev gcc

RUN apk add python3-dev musl-dev

RUN mkdir /docker-workspace
COPY . /docker-workspace

WORKDIR /docker-workspace

RUN pip install -r requirements.txt
CMD python -m workshop_app.main
