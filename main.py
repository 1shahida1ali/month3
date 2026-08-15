# pip install aiogram
# pip install python-decouple

from decouple import config

from aiogram import Bot, Dispatcher, Router, F
import asyncio
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import logging


token = config('BOT_TOKEN')

router = Router()

@router.message(Command('start'))
async def start_command(message: Message, bot: Bot):
    await message.answer('Привет. Как дела?')
    await bot.send_message(chat_id=message.chat.id, text='Приветствую!')

@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('/start - старт бота \n/help - помощник ')

@router.message(F.text == 'привет')
async def hello_command(message: Message):
    await message.answer('Hello')

@router.message(Command('mem'))
async def mem_command(message: Message, bot:Bot):
    photo = FSInputFile('media/mem-2.png')    
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

@router.message(F.text)
async def echo(message:Message):
    await message.answer(f'такой команды нет - {message.text}')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

