import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from secret import TOKEN

from euroopt import get_data_euroopt
from groshyk import get_data_groshyk
from hit import get_data_hit

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'старт', 'Старт'], )
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        'Евроопт',
        'Грошик',
        'Хит',
    ]
    keyboard.add(*buttons)
    await message.answer(text='Выберите сеть магазинов', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Меню', 'меню']))
async def euroopt(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = [
        'Евроопт',
        'Грошик',
        'Хит',
    ]
    keyboard.add(*buttons)
    await message.answer(text='Выберите сеть магазинов', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Евроопт', 'евроопт']))
async def euroopt(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add('Меню')
    data = get_data_euroopt()
    for i in data:
        text = i['src']
        await message.answer(text=text, reply_markup=keyboard)


@dp.message_handler(Text(equals=['Грошик', 'грошик']))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add('Меню')
    data = get_data_groshyk()
    for i in data:
        if 'https://groshyk.by/' not in i[0]["src"]:
            text = f'https://groshyk.by/{i[0]["src"]}'
        else:
            text = i[0]["src"]
        await message.answer(text=text, reply_markup=keyboard)


@dp.message_handler(Text(equals=['Хит', 'хит']))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add('Меню')
    data = get_data_hit()
    for i in data:
        text = i[0]["src"]
        await message.answer(text=text, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
