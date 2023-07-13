from aiogram import html, types
from aiogram.fsm.context import FSMContext

from aiogram_bot import states
from aiogram_bot.db.db_api import Repo


async def start(msg: types.Message, state: FSMContext, repo: Repo) -> None:
    if msg.from_user is None:
        return
    m = [
        f'Hello, <a href="tg://user?id={msg.from_user.id}">{html.quote(msg.from_user.full_name)}</a>'
    ]
    await msg.answer("\n".join(m))
    await state.set_state(states.user.UserMainMenu.menu)
