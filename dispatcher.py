from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Dispatcher, Bot, types

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
