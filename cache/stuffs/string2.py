from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


button1 = [
    [
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇ ", url=f"https://t.me/Abishnoi_bots"),
        InlineKeyboardButton(text="💥 ᴀᴅᴅ ᴍᴇ 💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", callback_data="repo_k"),
    ],                
    [                    
        InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help_"),
    ],
]


button2 = [
    [
        InlineKeyboardButton(text="ɴᴏʀᴍʟᴀ!", callback_data="basic_"),
        InlineKeyboardButton(text="ᴘʟᴀʏ!", callback_data="admin_cmd"),
    ],
    [
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close_"),
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="HOME"),
    ],
]



button3 = [
    [
        InlineKeyboardButton(text="Source", url="https://github.com/KingAbishnoi/AkMusic"),
        InlineKeyboardButton(text="•ʙᴀᴄᴋ•", callback_data="HOME"),
    ],
]


button4 = [
    [
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close_"),
        InlineKeyboardButton(text="•ʙᴀᴄᴋ•", callback_data="help_"),
    ],
]





