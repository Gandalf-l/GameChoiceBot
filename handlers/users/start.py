from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text
from loader import dp
from utils.misc import rate_limit

from handlers.users.btm import start, subscribe, unsubscribe
from handlers.users.test import enter_test


@rate_limit(5, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: Message):
  await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=start)


@dp.message_handler(Text(equals=["Subscription"]))
async def get_food(message: Message):
  await message.answer(f"Subscription Menu", reply_markup=subscribe)


@dp.message_handler(Text(equals=["Recommend"]))
async def get_food(message: Message):
  await enter_test(message)


@dp.message_handler(Text(equals=["Subscribe to newsletter"]))
async def get_food(message: Message):
  await message.answer(f"You subscribe to newsletter", reply_markup=unsubscribe)

@dp.message_handler(Text(equals=["Unsubscribe to newsletter"]))
async def get_food(message: Message):
  await message.answer(f"You unsubscribe to newsletter", reply_markup=subscribe)

@dp.message_handler(Text(equals=["Back"]))
async def get_food(message: Message):
  await message.answer(f"Start menu", reply_markup=start)
