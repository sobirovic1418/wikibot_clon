import logging

from aiogram import Bot,Dispatcher,executor,types

API_TOKEN="8142754108:AAEPn6c4c_HS99J9MREDW7k_cws9q4Kl38A"
logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)