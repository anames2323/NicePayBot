from aiogram import Router
from aiogram.types import CallbackQuery
from db import get_balance, change_balance

router = Router()

@router.callback_query(lambda c: c.data=="withdraw")
async def withdraw(c: CallbackQuery):
    bal = await get_balance(c.from_user.id)
    if bal < 1:
        await c.message.answer("❌ Недостаточно средств")
        return
    await change_balance(c.from_user.id, -1, ttype="withdraw")
    await c.message.answer("📤 Запрос на вывод создан (демо)")
