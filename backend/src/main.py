import asyncio
from asyncio import Future

from Webserver import Webserver
from Database import Database


async def main():
    webserver = Webserver()
    await webserver.run_server()
    db = Database()
    await db.check_for_db()
    print(await db.get_user_data())
    await Future()

if __name__ == '__main__':
    asyncio.run(main())
