from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💼 Профиль", callback_data="profile")],
    [InlineKeyboardButton(text="💰 Пополнить", callback_data="deposit")],
    [InlineKeyboardButton(text="📤 Вывод", callback_data="withdraw")],
    [InlineKeyboardButton(text="👥 Перевод", callback_data="transfer")],
    [InlineKeyboardButton(text="📜 История", callback_data="history")],
    [InlineKeyboardButton(text="🛡 Админ", callback_data="admin")]
])

