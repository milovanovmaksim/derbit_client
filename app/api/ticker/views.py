from aiohttp_apispec import docs, querystring_schema, response_schema
from api.web.bases import View

from api.ticker.schemas import (TickerRequestSchema,
                                ListTickerResponseSchema,
                                PriceTickerResponseSchema)
from api.web.utils import json_response
from database.database import Database
from models.ticker import TickerModel


class ListTickerView(View):
    @docs(tags=["tickers"], summary="Get list tickers.")
    @querystring_schema(TickerRequestSchema)
    @response_schema(ListTickerResponseSchema)
    async def get(self):
        """
        Вью-метод для GET-запроса.
        Метод декорируется "@querystring_schema", "@docs" с целью добавления информации о запросе
        в спецификацию Swagger и промежуточное программное обеспечение validation_middleware для валидации данных.

        Returns:
            _type_: Возвращает экземпляр класса aiohttp.web_response.Response.
        """
        query = self.query
        database: Database = self.request.app["database"]
        tickers = await TickerModel.get_tickers(ticker=query["ticker"], database=database)
        return json_response(schema=ListTickerResponseSchema(), data={"tickers": tickers})


class LastTickerPrice(View):
    @docs(tags=["tickers"], summary="Get last ticker price.")
    @querystring_schema(TickerRequestSchema)
    @response_schema(PriceTickerResponseSchema)
    async def get(self):
        """
        Вью-метод для GET-запроса.
        Метод декорируется "@querystring_schema", "@docs" с целью добавления информации о запросе
        в спецификацию Swagger и промежуточное программное обеспечение validation_middleware для валидации данных.

        Returns:
            _type_: Возвращает экземпляр класса aiohttp.web_response.Response.
        """
        query = self.query
        database: Database = self.request.app["database"]
        last_price = await TickerModel.get_last_price(ticker=query["ticker"], database=database)
        return json_response(schema=PriceTickerResponseSchema(), data={"last_price": last_price})
