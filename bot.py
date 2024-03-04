import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from router import router as all_routers
from aiogram.types import BotCommand

load_dotenv('.env')


async def main() -> None:

    bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    commands = [
        BotCommand(command="start", description="touch to start the bot"),
        BotCommand(command="vocabulary", description="touch to learn the vocabulary"),
    ]

    await bot.set_my_commands(commands)

    dp = Dispatcher()
    dp.include_router(all_routers)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
