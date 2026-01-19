from aiogram import Router
from aiogram.types import CallbackQuery
from crypto_pay import create_invoice

router = Router()

@router.callback_query(lambda c: c.data=="deposit")
async def deposit(c: CallbackQuery):
    inv = await create_invoice(10, "USDT", payload=str(c.from_user.id))
    await c.message.answer(f"💰 Оплатить:\\n{inv['result']['pay_url']}")

