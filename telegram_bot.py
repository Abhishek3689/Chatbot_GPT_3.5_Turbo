import os
import sys
from dotenv import load_dotenv
import openai
from aiogram import Bot,Dispatcher,executor,types

class Reference:
    '''
     A class to store previously input text 
    '''
    def __init__(self):
        self.response=""

load_dotenv()
#openai.api_key=os.getenv("OpenAI_API_KEY")
Token=os.getenv("TOKEN")
reference=Reference()

# Model Name
model_name="gpt-3.5-turbo"

## Initialize the bot and dispatcher
bot=Bot(Token)
dispatcher=Dispatcher(bot)

def clear_past_text():
    '''  
    will clear all previous info from memory
    '''
    reference.response=""

@dispatcher.message_handler(commands=['start'])
async def welcome(message:types.Message):
    ''' 
    This function will work when you provide start command
    '''
    await message.reply("Hi \nI am Telegram Bot \Created by Abhishek Nishad \nHow May I help you")

@dispatcher.message_handler(commands=['clear'])
async def clear_history(message:types.Message):
    '''
    this will clear the history
    '''
    clear_past_text()
    await message.reply("I have cleared all previous conversation")

@dispatcher.message_handler(commands=['help','menu'])
async def menu_option(message:types.Message):
    '''
    handler to display the help menu
    '''
    menu_list="""
    Hi!\n I am telebot created by Abhishek \n\nChoose from below menu option\n
    * start : To start the Conversation
    * clear : To clear previous chat history
    * help  : To go to Main Menu
    * menu  : To go to Menu option
    """
    await message.reply(menu_list)


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)

