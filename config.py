from decouple import config
from aiogram import Bot, Dispatcher

token = config('BOT_TOKEN')

bot = Bot(token=token)

dp = Dispatcher()