from aiogram import Router
from aiogram.filters import CommandStart, StateFilter, Text

from aiogram_bot import states
from aiogram_bot.filters import ChatTypeFilter

from aiogram_bot.handlers.user import start


def prepare_router() -> Router:
    user_router = Router()
    user_router.message.filter(ChatTypeFilter("private"))

    user_router.message.register(start.start, CommandStart())
    user_router.message.register(
        start.start, Text("🏠В главное меню"), StateFilter(states.user.UserMainMenu.menu)
    )

    return user_router
