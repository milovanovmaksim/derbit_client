import asyncio
from database.config import setup_database

from derbit_client.ticker.list_index_name import ListIndexName
from derbit_client.ticker.ticker import StorageTicker
from derbit_client.client import Client
from apscheduler.schedulers.asyncio import AsyncIOScheduler


def main():
    database = setup_database("./config.yml")
    client = Client(
        StorageTicker(
            ListIndexName(index_names=["btc_usd", "eth_usd"]),
            database=database)
        )
    scheduler: AsyncIOScheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(client.run, trigger="interval", seconds=60)
    scheduler.start()
    print("Start client\nPress Ctrl+C for exit")
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
