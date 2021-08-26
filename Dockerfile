# syntax=docker/dockerfile:1

FROM python:3.9.2
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]