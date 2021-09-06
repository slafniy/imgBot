# syntax=docker/dockerfile:1

FROM centos:latest

RUN dnf install python39 -y

WORKDIR opt/img-bot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

COPY ./app .


ENTRYPOINT ["python3", "main.py"]