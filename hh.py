"""


https://api.dictionaryapi.dev/api/v2/entries/en/<word>

"""
import logging
import requests
from googletrans import Translator
from aiogram import Bot,Dispatcher,executor,types
import os
tokenn = '1900084854:AAGQmTzjuJqqI-Sofko0IPQ0wEQqtQk3OAA'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=tokenn)
dp = Dispatcher(bot)
translator = Translator()

@dp.message_handler(commands=['start', 'help'])
async def javob(message: types.Message):


        await message.reply('salom')


@dp.message_handler()
async def message_javob(message: types.Message):
    til = translator.detect(message.text).lang
    print(til)

    if til == 'uz':
        await message.reply(translator.translate(message.text, src='uz',dest='ru').text)
    else:
        dest = 'ru'
        await message.reply(translator.translate(message.text, dest).text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
