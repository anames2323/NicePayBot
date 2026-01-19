from aiogram import Router
from aiogram.types import CallbackQuery
from db import change_balance, get_balance

router = Router()

@router.callback_query(lambda c: c.data=="transfer")
async def transfer(c: CallbackQuery):
    bal = await get_balance(c.from_user.id)
    if bal < 1:
        await c.message.answer("❌ Недостаточно средств")
        return
    await change_balance(c.from_user.id, -1, ttype="transfer")
    await c.message.answer("👥 Перевод выполнен (демо)")
