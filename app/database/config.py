from dataclasses import dataclass

import yaml

from database.database import Database


@dataclass
class DatabaseConfig:
    """
    Класс, содержащий конфигурационные настройки базы данных.
    """
    host: str
    port: int
    user: str
    password: str
    database: str


def setup_config(config_path: str) -> DatabaseConfig:
    """
    Устанавливает конфигурационные настройки базы даннах.
    Args:
        config_path (str): Путь к конфигурационному файлу.
    Returns: Возвращает экземпляр класса DatabaseConfig.
    """
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)

    return DatabaseConfig(**raw_config["database"])


def setup_database(config_path: str) -> Database:
    """
    Устанавливает экземпляр класса Database для текущего экземпляра приложения Application.
    """
    config: DatabaseConfig = setup_config(config_path)
    database = Database(config)
    database.connect()
    return database

