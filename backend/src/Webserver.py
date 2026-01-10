import asyncio
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn.config import Config
from uvicorn.server import Server

FRONTEND_DIST = Path(__file__).parent.parent / "dist"


class Webserver:
    @staticmethod
    def test_get(path: str):
        return {"message": f"You requested the path: {path}"}

    def __init__(self):
        self.app = FastAPI()
        self.app.get("/api/test/{path}")(self.test_get)

        if os.getenv("DEPLOYMENT_MODE") == "docker":
            self.app.mount(
                "/",
                StaticFiles(directory=FRONTEND_DIST, html=True),
                name="spa",
            )


    async def run_server(self):
        """
        Starts the api server.
        """
        config = Config(self.app, host="0.0.0.0", port=8000, log_config=None)
        server = Server(config)
        _ = asyncio.create_task(server.serve())
