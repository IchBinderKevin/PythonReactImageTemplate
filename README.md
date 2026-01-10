# Python + React template repository
This repository provides a very simple starter template for building applications with a web-interface using Python for the backend and React for the frontend while combining them into one docker image for easy deployment.
It basically lets fast api serve the built react project.

This is not really a "production ready" template and just serves as a jumping off point (mainly for myself) so I can get new ideas that require a frontend up an running quite quickly using docker.
Feel free to use this if you see any merit in it, but be aware that this template is not being kept up to date or update at all.

## Project Structure
The project is structured into two main directories:
- backend/: Contains the Python backend code. Uses FastAPI as the web framework, and Uvicorn as the ASGI server. Also relies on uv for dependency management.
- frontend/: Contains the React frontend code. Uses Vite as the build tool, typescript and tailwindcss for styling.
