from typing import TYPE_CHECKING, Any, Sequence

from aiohttp.web_exceptions import HTTPServerError

from sqlalchemy import Column, Integer, Select, String, select
from sqlalchemy.sql.functions import max as sa_max
from sqlalchemy.engine import Result

from database.sqlalchemy_base import db

if TYPE_CHECKING:
    from database.database import Database


class TickerModel(db):
    __tablename__ = "tickers"
    idx = Column(Integer, primary_key=True)
    ticker = Column(String(8), nullable=False)
    price = Column(Integer, nullable=False)
    timestamp = Column(Integer, nullable=False)

    @staticmethod
    async def get_tickers(ticker: str, database: "Database") -> list[dict[str, Any]]:
        query = select(TickerModel).where(TickerModel.ticker == ticker)
        if database.session:
            async with database.session() as session:
                result: Result[TickerModel]  = await session.execute(query)
                await session.commit()
                ticker_models: Sequence[TickerModel] = result.scalars().all()
                tickers = [{
                    "idx": ticker.idx,
                    "ticker": ticker.ticker,
                    "price": ticker.price,
                    "timestamp": ticker.timestamp
                    } for ticker in ticker_models]
                return tickers
        raise HTTPServerError()

    @staticmethod
    async def get_last_price(ticker: str, database: "Database") -> int:
        sub_query = select(sa_max(TickerModel.timestamp)).where(TickerModel.ticker == ticker).scalar_subquery()
        query: Select = (select(TickerModel.price)
                         .where(
                             TickerModel.timestamp == sub_query,
                             TickerModel.ticker == ticker))
        if database.session:
            async with database.session() as session:
                result: Result[TickerModel] = await session.execute(query)
                last_price = result.scalar_one()
                return last_price

        raise HTTPServerError()
