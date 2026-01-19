from aiogram import Router
from aiogram.types import CallbackQuery
from db import get_all_users
from config import ADMIN_IDS

router = Router()

@router.callback_query(lambda c: c.data=="admin")
async def admin_panel(c: CallbackQuery):
    if c.from_user.id not in ADMIN_IDS:
        await c.message.answer("❌ Не админ")
        return
    users = await get_all_users()
    msg = "\n".join([f"{u[0]}: {u[1]} USDT" for u in users]) or "Нет пользователей"
    await c.message.answer(f"🛡 Пользователи:\n{msg}")
