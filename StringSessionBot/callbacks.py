import traceback
from data import Data
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
#from StringSessionBot.generate import generate_session, ask_ques, buttons_ques


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user.mention
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
    elif query == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif query == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )

ERROR_MESSAGE = "ᴏᴏᴘꜱ! ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀʀᴇᴅ! \ɴ\ɴ**ᴇʀʀᴏʀ** : {} " \
"\ɴ\ɴᴘʟᴇᴀꜱᴇ ᴠɪꜱɪᴛ @V_VIP_OWNER ɪꜰ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴅᴏᴇꜱɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ " \
"ꜱᴇɴꜱɪᴛɪᴠᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ʏᴏᴜ ɪꜰ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴛʜɪꜱ ᴀꜱ " \
"ᴛʜɪꜱ ᴇʀʀᴏʀ ᴍᴇꜱꜱᴀɢᴇ ɪꜱ ɴᴏᴛ ʙᴇɪɴɢ ʟᴏɢɢᴇᴅ ʙʏ ᴜꜱ!"
