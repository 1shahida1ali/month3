from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from config import bot

router_commands = Router()

@router_commands.message(Command('start'))
async def start_command(message: Message, bot):
    await message.answer('Привет. Напиши своё имя ')
    await bot.send_message(chat_id=message.chat.id, text='Приветствую!')


@router_commands.message(Command('help'))
async def help_command(message: Message):
    await message.answer('/start - старт бота \n/help - помощник ')


@router_commands.message(F.text == 'привет')
async def hello_command(message: Message):
    await message.answer('Hello')


@router_commands.message(Command('mem'))
async def mem_command(message: Message, bot):
    photo = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)