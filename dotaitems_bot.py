import json
from pyexpat.errors import messages
from aiogram import Bot, Dispatcher, dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
import os
import time

api_token = 'UR TOKEN'

bot = Bot(token=api_token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['😎Immortal', '👾Mythical', '👽Legendary and Arcana👹']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выберите категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='😎Immortal'))
async def get_discount_immortal(message: types.Message):
    await message.answer('Погоди...')

    collect_data(rarity_item=5)

    with open('result.json') as file:
        data = json.load(file)
    
    for index, item in enumerate(data):
        card = f'{hlink(item.get("quality"), item.get("img"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("price")}🤑'
        
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='👾Mythical'))
async def get_discount_immortal(message: types.Message):
    await message.answer('Погоди...')

    collect_data(rarity_item=3)

    with open('result.json') as file:
        data = json.load(file)
    
    for index, item in enumerate(data):
        card = f'{hlink(item.get("quality"), item.get("img"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("price")}🤑'
        
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)

@dp.message_handler(Text(equals='👽Legendary and Arcana👹'))
async def get_discount_immortal(message: types.Message):
    await message.answer('Погоди...')

    collect_data(rarity_item=6)
    collect_data(rarity_item=7)

    with open('result.json') as file:
        data = json.load(file)
    
    for index, item in enumerate(data):
        card = f'{hlink(item.get("quality"), item.get("img"))}\n' \
            f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
            f'{hbold("Цена: ")}${item.get("price")}🤑'
        
        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
