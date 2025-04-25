import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from utils import get_car_image_url

# .env fayldan tokenni yuklash
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Bot obyektini yaratish
bot = Bot(token=BOT_TOKEN)

# Dispatcher obyektini bot bilan birga yaratish (aiogram 3.x)
dp = Dispatcher()

# Logger sozlash
logging.basicConfig(level=logging.INFO)

# Qiziqarli ta'riflar lug'ati
funny_descriptions = {
    "bmw": "BMW — Bu Mashina Waqt mashinasiga o‘xshaydi! 🚀",
    "tesla": "Tesla — o‘zini mashina deb o‘ylagan robot! 🤖⚡️",
    "nexia": "Nexia — O‘zbekiston yo‘llarining haqiqiy qiroli! 👑",
    "bugatti": "Bugatti — tezlikni nonushta qilib yeydi! 💨",
}

# /start komandasiga javob
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer(
        "Salom! Men AvtoGuru — mashinalar olamidagi yo‘lko‘rsatgingman! 🚘\n\n"
        "Menga mashina nomini yozing — rasm va biroz kulgili ma’lumot beraman! 😎"
    )

# Mashina nomiga mos javob
@dp.message()
async def car_handler(message: Message):
    car_name = message.text.strip().lower()
    image_url = await get_car_image_url(car_name)

    desc = funny_descriptions.get(car_name, f"{car_name.capitalize()} — Juda zo‘r tanlov! 🚗")

    if image_url:
        await message.answer_photo(photo=image_url, caption=desc)
    else:
        await message.answer(f"Kechirasiz, {car_name} mashinasini topolmadim... 🧐 Yana urinib ko‘ring!")

# Botni ishga tushurish
async def main():
    print("✅ Bot ishga tushdi!")
    await dp.start_polling(bot)

# Asosiy ishga tushirish
if __name__ == "__main__":
    asyncio.run(main())