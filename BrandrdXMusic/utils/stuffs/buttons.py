from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("🤖𝐂ʜᴀʀ𝐆𝐏𝐓💬", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("🕰️𝐇ɪꜱᴛᴏʀʏ📖", callback_data="mplus HELP_History"),InlineKeyboardButton("🎞️𝐑ᴇᴇʟ🎥", callback_data="mplus HELP_Reel")],
    [InlineKeyboardButton("🏷️𝐓ᴀɢ-𝐀ʟʟ👥", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("ℹ️𝐈ɴꜰᴏ📚", callback_data="mplus HELP_Info"),InlineKeyboardButton("✨𝐄xᴛʀᴀ🎁", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("💑𝐂ᴏᴜᴘʟᴇ'ꜱ💖", callback_data="mplus HELP_Couples"),
    InlineKeyboardButton("🎬𝐀ᴄᴛɪᴏɴ🎯", callback_data="mplus HELP_Action"),InlineKeyboardButton("🔍𝐒ᴇᴀʀᴄʜ🗂️", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("🔤𝐅ᴏɴᴛ🎨", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("🤖𝐁ᴏᴛꜱ⚙️", callback_data="mplus HELP_Bots"),InlineKeyboardButton("🛰️𝐓-𝐆ʀᴀᴘʜ🗒️", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("🧩𝐒ᴏᴜʀᴄᴇ💻", callback_data="mplus HELP_Source"),
    InlineKeyboardButton("🎲𝐓ʀᴜᴛʜ-𝐃ᴀʀᴇ🎯", callback_data="mplus HELP_TD"),InlineKeyboardButton("📝𝐐ᴜɪᴢ🧠", callback_data="mplus HELP_Quiz")], 
    [InlineKeyboardButton("🎙️𝐓ᴛꜱ🔊", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("📻𝐑ᴀᴅɪᴏ🎶", callback_data="mplus HELP_Radio"),InlineKeyboardButton("💌𝐐ᴜᴏᴛʟʏ✍️", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("◁", callback_data=f"settings_back_helper"),
     InlineKeyboardButton("↻ ʙᴀᴄᴋ ↻", callback_data=f"mbot_cb"), 
    InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper"),
    ]]
