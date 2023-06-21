from typing import TYPE_CHECKING, Any, Optional
from asyncio import create_task, Task, gather

from sqlalchemy import insert

from models.ticker import TickerModel


if TYPE_CHECKING:
    from derbit_client.ticker.list_index_name import ListIndexName
    from database.database import Database


class StorageTicker:
    def __init__(self, list_index_name: "ListIndexName", database: "Database"):
        self._list_index_name = list_index_name
        self.database = database

    async def run(self):
        tickers = await self._list_index_name.run()
        await self._save_to_db(tickers)

    async def _save_to_db(self, tickers):
        for ticker in tickers:
            create_task(self._innsert_ticker(ticker=ticker))

    async def _innsert_ticker(self, ticker: dict[str, Any]) -> Optional[TickerModel]:
        query = insert(TickerModel).returning(TickerModel).values(**ticker)
        if not self.database.session:
            self.database.connect()
        async with self.database.session() as session:  # type: ignore
            result = await session.execute(query)
            await session.commit()
            ticker_model = result.scalar_one_or_none()
            return ticker_model
