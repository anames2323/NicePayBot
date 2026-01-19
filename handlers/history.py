from aiogram import Router
from aiogram.types import CallbackQuery
from db import get_transactions

router = Router()

@router.callback_query(lambda c: c.data=="history")
async def history(c: CallbackQuery):
    txs = await get_transactions(c.from_user.id)
    msg = "\n".join([f"{t[1]}: {t[0]}" for t in txs]) or "Нет транзакций"
    await c.message.answer(f"📜 Последние транзакции:\n{msg}")
