import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from secret import TOKEN

from euroopt import get_red_price, get_blackfriday_price
import groshyk

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'старт', 'Старт', 'меню', 'Меню'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ['Евроопт', 'Грошик']
    keyboard.add(*buttons)
    await message.answer(text='Выберите сеть магазинов', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Евроопт', 'евроопт']))
async def euroopt(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ['Красная цена', 'Черная пятница']
    keyboard.add(*buttons)
    await message.answer(text='Выберите акцию', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Красная цена', 'красная цена']))
async def euroopt(message: types.Message):
    data = get_red_price()
    for i in data:
        text = i['src']
        await message.answer(text=text, parse_mode='HTML')


@dp.message_handler(Text(equals=['Черная пятница', 'черная пятница', 'Чёрная пятница', 'чёрная пятница']))
async def euroopt(message: types.Message):
    data = get_blackfriday_price()
    for i in data:
        text = i['src']
        await message.answer(text=text, parse_mode='HTML')


@dp.message_handler(Text(equals=['Грошик', 'грошик']))
async def start(message: types.Message):
    data = groshyk.get_data()
    for i in data:
        if 'https://groshyk.by/' not in i[0]["src"]:
            text = f'https://groshyk.by/{i[0]["src"]}'
        else:
            text = i[0]["src"]
        await message.answer(text=text, parse_mode='HTML')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
