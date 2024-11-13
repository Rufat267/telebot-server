from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


qrcode  = ReplyKeyboardMarkup(resize_keyboard=True)

menu = KeyboardButton(text='🍽Menu🍽')
qrcode.add(menu)