from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext 
# from keybords import *
from state import router as state_router
from service import *
from conection import *


import os
import asyncio




load_dotenv()



token_bot = os.getenv("BOT_TOKEN")



bot = Bot(token=token_bot)


dp = Dispatcher()











async def  main():
    await create_table()
    print("Table created!")
    dp.include_router(state_router)
    print("Bot started!")
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())