# syntax=docker/dockerfile:1

FROM python:3.9.7

WORKDIR opt/img-bot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

COPY ./app .


ENTRYPOINT ["python3", "img_bot.py"]