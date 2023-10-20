import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()
api_token=os.getenv("TOKEN")
#print(api_token)

#configure loggin
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

## Initialize bot and dispathcer
bot=Bot(token=api_token)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply(f"Hello! \nI am Echobot \npowered by Abhishek")



@dp.message_handler()
async def echo_message(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
