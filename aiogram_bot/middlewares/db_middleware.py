from typing import Callable, Any, Awaitable

import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

from aiogram_bot.db.db_api import Repo


class DataBaseMiddleware(BaseMiddleware):
    def __init__(self, db: asyncpg.Pool):
        self.db = db
        super(DataBaseMiddleware, self).__init__()

    async def __call__(
            self,
            handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: dict[str, Any],
    ) -> Any:
        async with self.db.acquire():
            repo = Repo(self.db)
            data["repo"] = repo
            r = await handler(event, data)
        return r
