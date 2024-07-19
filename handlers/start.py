from aiogram import Router
from aiogram.types import Message
from aiogram.types.chat_member import CommandStart


start_router: Router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
       await message.answer(f"Hello, {(message.from_user.full_name)}!")
