from typing import TYPE_CHECKING

from database.database import Database

if TYPE_CHECKING:
    from aiohttp.web import Application
    from database.config import DatabaseConfig


def setup_database(app: "Application"):
    """
    Устанавливает экземпляр класса Database для текущего экземпляра приложения Application.
    Также, добавляет методы Database.connect и Database.disconnect в сигналы.

    Args:
        app (Application): _description_
    """
    config: "DatabaseConfig" = app["config"].database
    database = Database(config)
    app["database"] = database
    database.connect()
    app.on_cleanup.append(app["database"].disconnect)
