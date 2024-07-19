
from aiogram import Router, F
from aiogram.types import Message, chat_nember_upadate
from aiogram.types.chat_member import ChatMember
from googletrans import Translator

trans_router: Router=Router()

translator=Translator()

def trans_bot(text):
    try:
        result = translator.translate(text)
        return result.text
    except:
        return f"kechirasiz ({text}) sozni tarjima qila olmadim"
    
    
@trans_router.message()
async def trans_handler(msg: Message):
    text = msg.text
    await msg.reply(trans_bot(msg.text))
