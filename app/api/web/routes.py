from typing import TYPE_CHECKING

from api.ticker.routes import setup_routes as ticker_setup_routes


if TYPE_CHECKING:
    from api.web.app import Application


def setup_routes(app: "Application"):
    """
    Устанавливает конечные точки веб-приложения.

    Args:
        app (Application): _description_
    """
    ticker_setup_routes(app)

