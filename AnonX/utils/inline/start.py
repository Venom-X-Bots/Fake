from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ Sᴜᴘᴘᴏʀᴛᴇʀ ❣", url=f"https://t.me/BotBugs/2"
            ),
            InlineKeyboardButton(
                text="🥀 Mᴀɪɴᴛᴀɪɴᴇʀ 🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ CʜɪᴛCʜᴀᴛ ✨", url=f"https://t.me/AwesomeBlossome"
            )
        ],
     ]
    return buttons
