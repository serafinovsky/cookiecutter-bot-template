FROM python:3.11.7-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y nano \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt && mkdir -p /var/log/gunicorn && python manage.py collectstatic --no-input -c
