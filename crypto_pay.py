import aiohttp
from config import CRYPTO_PAY_TOKEN

BASE_URL = "https://pay.crypt.bot/api"
HEADERS = {"Crypto-Pay-API-Token": CRYPTO_PAY_TOKEN}

async def create_invoice(amount, asset="USDT", payload=None):
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.post(
            f"{BASE_URL}/createInvoice",
            json={
                "asset": asset,
                "amount": amount,
                "payload": payload
            }
        ) as r:
            return await r.json()

