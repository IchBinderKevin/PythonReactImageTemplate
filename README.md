# Python + React template repository
This repository provides a very simple starter template for building applications with a web-interface using Python for the backend, sqlite for storage and React for the frontend while combining them into one docker image for easy deployment.
It basically lets fast api serve the built react project.

This is not really a "production ready" template and just serves as a jumping off point (mainly for myself) so I can get new ideas that require a frontend up an running quite quickly using docker.
Feel free to use this if you see any merit in it, but be aware that this template is not being kept up to date or update at all.

## Project Structure
The project is structured into two main directories:
- backend/: Contains the Python backend code. Uses FastAPI as the web framework, and Uvicorn as the ASGI server. Also relies on uv for dependency management. Comes with a small async sqlite database setup as well using SQLAlchemy as an ORM and alembic for migrations. It also comes with a simple router -> service structure.
- frontend/: Contains the React frontend code. Uses Vite as the build tool, typescript and tailwindcss for styling.

## Envs
DEPLOYMENT_MODE:
  if set to "docker" the backend will serve the react files. If not it will....not. During development they are treated as two different services that should be started individually. Vite then proxies requests to /api/* to the specified address (where the backend should be running). Make sure to change this proxy address if you run the backend on a different port!
DB_PATH:
    path to the sqlite database file. Default is "./db/db.db" meaning you can mount a volume to /app/db to persist the database.
