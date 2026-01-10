# -------- frontend build --------
FROM node:20-alpine AS frontend

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

# copy built frontend
COPY --from=frontend /frontend/dist ./dist

EXPOSE 8000
ENV DEPLOYMENT_MODE="docker"
CMD ["uv", "run", "python", "src/main.py"]
