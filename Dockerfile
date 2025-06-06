FROM python:3.13.4-slim-bookworm AS builder
EXPOSE 8000
WORKDIR /app
RUN pip3 install uv
COPY . /app
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN uv pip install --system --extra dev -r pyproject.toml
