from aiogram import Router
from aiogram.filters import CommandStart
from keyboards import main_kb
from db import add_user

router = Router()

@router.message(CommandStart())
async def start(message):
    await add_user(message.from_user.id)
    await message.answer("🚀 Добро пожаловать в NicePay Bot", reply_markup=main_kb)

