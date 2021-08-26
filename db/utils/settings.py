import socket
from typing import Any, Dict

from pydantic import BaseModel, BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import json
import re
from functools import partial

from pydantic.json import custom_pydantic_encoder

from db import metadata

JsonSerializer = partial(
    json.dumps,
    ensure_ascii=False,
    indent=True,
    default=partial(custom_pydantic_encoder, {type(re.compile('')): lambda v: v.pattern}),
)


class BaseDBModel(BaseModel):
    url: str
    engine_config: Dict[str, Any] = {}
    echo: int = 0

    @property
    def engine(self) -> Engine:
        self.engine_config.setdefault('json_serializer', JsonSerializer)
        self.engine_config.setdefault('executemany_mode', 'values')
        self.engine_config.setdefault('connect_args', {})
        self.engine_config['connect_args'].setdefault('application_name', socket.gethostname())
        return create_engine(str(self.url), **self.engine_config, echo=self.echo)

    def setup_db(self) -> None:
        pass


class DBSettings(BaseDBModel, BaseSettings):
    class Config:
        env_prefix = 'DB_'

    def setup_db(self) -> None:
        metadata.bind = self.engine
