from typing import TYPE_CHECKING


from api.ticker.views import ListTickerView, LastTickerPrice

if TYPE_CHECKING:
    from aiohttp.web import Application
    from aiohttp_cors import CorsConfig


def setup_routes(app: "Application"):
    """
    Устанавливает конечные точки для манипуляции данными в таблице "mp3_files" базы данных.
    """
    cors: "CorsConfig" = app["cors"]
    cors.add(app.router.add_view("/tickers.list", ListTickerView))
    cors.add(app.router.add_view("/tickers.last_price", LastTickerPrice))
