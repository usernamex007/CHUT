from data import Data
from pyrogram import Client, filters
from env import ALIVE_PIC

from pyrogram.types import InlineKeyboardMarkup, Message


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_photo(
        msg.chat.id, 
        ALIVE_PIC,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )


# Help Message
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    await bot.send_photo(
        msg.chat.id, 
        ALIVE_PIC, 
        Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# About Message
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_photo(
        msg.chat.id, 
        ALIVE_PIC,
        Data.ABOUT,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
