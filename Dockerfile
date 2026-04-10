# -------- frontend build --------
FROM node:24-alpine AS frontend

WORKDIR /frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ .
RUN npm run build

# -------- backend runtime --------
FROM python:3.13-slim

# install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# copy backend dependency files
COPY backend/pyproject.toml backend/uv.lock ./

RUN uv sync --no-dev

# copy backend source
COPY backend/src ./src
COPY backend/alembic.ini ./

# copy built frontend
COPY --from=frontend /frontend/dist ./dist

# copy entrypoint script
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

# create data directory
RUN mkdir -p data

# set environment variables
ARG VERSION
ENV APP_VERSION=$VERSION

ENV DEPLOYMENT_MODE="docker"
ENV PYTHONUNBUFFERED=1

EXPOSE 3000

CMD ["./entrypoint.sh"]
