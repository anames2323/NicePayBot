#!/bin/bash
pip install -r requirements.txt
export BOT_TOKEN=$BOT_TOKEN
export CRYPTO_PAY_TOKEN=$CRYPTO_PAY_TOKEN
python bot.py
