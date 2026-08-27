from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router_fsm = Router()


class AddFilm(StatesGroup):
    title = State()
    genre = State()
    rating = State()


@router_fsm.message(Command("film"))
async def start_film(message: Message, state: FSMContext):
    await message.answer("🎬 Введите название фильма:")
    await state.set_state(AddFilm.title)


@router_fsm.message(Command("cancel"))
async def cancel_film(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Анкета отменена.\n"
        "Чтобы начать заново, напишите /film"
    )


@router_fsm.message(AddFilm.title)
async def film_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)

    await message.answer("🎭 Введите жанр фильма:")
    await state.set_state(AddFilm.genre)


@router_fsm.message(AddFilm.genre)
async def film_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)

    await message.answer("⭐ Введите оценку фильма от 1 до 10:")
    await state.set_state(AddFilm.rating)


@router_fsm.message(AddFilm.rating)
async def film_rating(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.answer(
            "❗ Оценка должна быть числом.\n"
            "Введите число от 1 до 10:"
        )
        return

    rating = int(message.text)

    if rating < 1 or rating > 10:
        await message.answer(
            "❗ Оценка должна быть от 1 до 10:"
        )
        return

    await state.update_data(rating=rating)

    data = await state.get_data()

    await message.answer(
        "✅ Фильм добавлен!\n\n"
        f"🎬 Название: {data['title']}\n"
        f"🎭 Жанр: {data['genre']}\n"
        f"⭐ Оценка: {data['rating']}/10"
    )

    await state.clear()
