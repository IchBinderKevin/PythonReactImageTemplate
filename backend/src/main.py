import asyncio
import os
from pathlib import Path

from common_constants import DATA_PATH, DEFAULT_DB_PATH
from webserver import Webserver


async def main():
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    if not os.path.exists(DEFAULT_DB_PATH):
        Path(DEFAULT_DB_PATH).touch()
    webserver = Webserver()
    await webserver.run_server()

if __name__ == '__main__':
    asyncio.run(main())
