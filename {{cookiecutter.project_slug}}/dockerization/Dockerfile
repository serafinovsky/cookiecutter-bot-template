{% if cookiecutter.python_version == "py311" %}FROM python:3.11.7-bullseye{% elif cookiecutter.python_version == "py312" %}FROM python:3.12.11-bullseye{% elif cookiecutter.python_version == "py313" %}FROM python:3.13.5-bullseye{% endif %}

ARG DEBIAN_FRONTEND=noninteractive
ENV UV_VERSION="0.7.13"

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y nano \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
COPY src/ .
RUN pip install uv==$UV_VERSION && uv sync --frozen --no-install-project --no-dev && mkdir -p /var/log/gunicorn && python manage.py collectstatic --no-input -c
