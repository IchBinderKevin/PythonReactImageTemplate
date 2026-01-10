import asyncio
from asyncio import Future

from Webserver import Webserver


async def main():
    webserver = Webserver()
    await webserver.run_server()
    await Future()

if __name__ == '__main__':
    asyncio.run(main())
