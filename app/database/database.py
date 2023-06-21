from typing import Any, Optional, TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.engine.url import URL

from .sqlalchemy_base import db

if TYPE_CHECKING:
    from database.config import DatabaseConfig


class Database:
    """
    Класс для соединения с базой данных.
    """
    def __init__(self, config: "DatabaseConfig"):
        self.config = config
        self._engine: Optional[AsyncEngine]
        self._db: Any
        self.session: Optional[async_sessionmaker[AsyncSession]] = None

    def connect(self, *args, **kwargs) -> None:
        """
        Создает объект класса AsyncSession.
        """
        self._db = db
        self._engine = create_async_engine(
            URL.create(
                drivername="postgresql+asyncpg",
                host=self.config.host,
                database=self.config.database,
                username=self.config.user,
                password=self.config.password,
                port=self.config.port,
                ),
            echo=False,
            future=True
        )
        self.session = async_sessionmaker(bind=self._engine, expire_on_commit=False, class_=AsyncSession)

    async def disconnect(self, *args, **kwargs) -> None:
        """
        Удаляет пул соединений, используемый текущей сессией self.session.
        """
        if self._engine:
            await self._engine.dispose()
