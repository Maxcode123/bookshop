FROM python:3.13.4-slim-bookworm AS builder

ENV DJANGO_SETTINGS_MODULE=bookshop.settings \
    PATH="/venv/bin/:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/venv \
    UV_NO_MANAGED_PYTHON=1 \
    UV_PYTHON_DOWNLOADS=never \
    VIRTUAL_ENV=/venv \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_CACHE_DIR=/app/.cache/uv \
    UV_FROZEN=1 \
    UV_REQUIRE_HASHES=1 \
    UV_VERIFY_HASHES=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

RUN uv venv $VIRTUAL_ENV

ARG BUILD_GROUPS=""

RUN --mount=type=cache,target=/app/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project --no-editable $BUILD_GROUPS

COPY bookshop /app/bookshop
COPY books /app/books
COPY utils /app/utils
COPY logs /app/logs
COPY tests /app/tests
COPY manage.py /app/

# FINAL IMAGE
FROM python:3.13.4-slim-bookworm

ARG PORT=8000

ENV DJANGO_SETTINGS_MODULE=bookshop.settings \
    PORT=${PORT} \
    PATH="/venv/bin/:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/venv

EXPOSE ${PORT}

WORKDIR /app

RUN <<EOT
    apt-get clean -y && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends libpq-dev gcc bash && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EOT

COPY --link --from=builder /venv /venv
COPY --link --from=builder /app/bookshop /app/bookshop
COPY --link --from=builder /app/books /app/books
COPY --link --from=builder /app/utils /app/utils
COPY --link --from=builder /app/logs /app/logs
COPY --link --from=builder /app/tests /app/tests
COPY --link --from=builder /app/manage.py /app/manage.py
