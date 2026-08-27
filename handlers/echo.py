from aiogram import F, Router
from aiogram.types import Message

router_echo = Router()

@router_echo.message(F.text)
async def echo(message: Message):
    await message.answer(f'Такой команды нет - {message.text}')