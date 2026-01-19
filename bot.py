import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from db import init_db
from handlers import start, profile, deposit, withdraw, transfer, history, admin

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(deposit.router)
    dp.include_router(withdraw.router)
    dp.include_router(transfer.router)
    dp.include_router(history.router)
    dp.include_router(admin.router)

    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

