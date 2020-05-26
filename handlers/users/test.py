from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states.test import Test

from handlers.users.btm import genres, price, platform, operatingSystem, languages

import requests
import json


@dp.message_handler(Command("recommend"), state=None)
async def enter_test(message: Message):
  await message.answer("You start test.\n"
                       "Question №1. \n\n"
                       "What game genres do you prefer? ", reply_markup=genres)
  # Вариант 1 - с помощью функции сет
  await Test.genre.set()

  # Вариант 2 - с помощью first
  # await Test.first()


@dp.message_handler(state=Test.genre)
async def answer_q1(message: Message, state: FSMContext):
  answer = [message.text]

  # Ваирант 2 получения state
  # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)

  # Вариант 1 сохранения переменных - записываем через key=var
  await state.update_data(genre=answer)

  # Вариант 2 - передаем как словарь
  # await state.update_data(
  #   {"answer1": answer}
  # )

  # Вариант 3 - через state.proxy
  # async with state.proxy() as data:
  #     data["answer1"] = answer
  # Удобно, если нужно сделать data["some_digit"] += 1
  # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать

  await message.answer("Question №2. \n\n"
                       "How much are you willing to pay for the game?", reply_markup=price)

  await Test.next()


@dp.message_handler(state=Test.price)
async def answer_q1(message: Message, state: FSMContext):
  answer = int(''.join(x for x in message.text if x.isdigit()))

  await state.update_data(price=answer)

  await message.answer("Question №3. \n\n"
                       "What is your platform?What is your platform?", reply_markup=platform)

  await Test.next()


@dp.message_handler(state=Test.platform)
async def answer_q1(message: Message, state: FSMContext):
  answer = message.text

  await state.update_data(platform=answer)

  await message.answer("Question №4. \n\n"
                       "What is your operating system?", reply_markup=operatingSystem)

  await Test.next()


@dp.message_handler(state=Test.operatingSystem)
async def answer_q1(message: Message, state: FSMContext):
  answer = message.text

  await state.update_data(operatingSystem=answer)

  await message.answer("Question №5. \n\n"
                       "Which languages do you prefer?", reply_markup=languages)

  await Test.next()


@dp.message_handler(state=Test.languages)
async def answer_q2(message: Message, state: FSMContext):
  # Достаем переменные
  answer = [message.text]
  await state.update_data(languages=answer)
  obj = {}
  async with state.proxy() as data:
    url = "https://topgame20200526105716.azurewebsites.net/api/TestRecommend/answer"
    for a in data:
      obj[a] = data[a]
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain'}
    ans = requests.post(url, data=json.dumps(obj), headers=headers)

    text = ''
    asd = json.loads(ans.text)
    for i, x in enumerate(asd):
      text += str(i + 1) + ") " + str(x['name']) + " - " + str(x['price']) + ' $\n'


  await message.answer(text, reply_markup=ReplyKeyboardRemove())

  # Вариант 1
  await state.finish()

  # Вариант завершения 2
  # await state.reset_state()

  # Вариант завершения 3 - без стирания данных в data
  # await state.reset_state(with_data=False)
