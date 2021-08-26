# syntax=docker/dockerfile:1

FROM centos:latest

RUN dnf install python39 firefox -y

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]