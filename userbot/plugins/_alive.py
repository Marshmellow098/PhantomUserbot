# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...

import os
import asyncio
import random
from telethon import events
from userbot.utils import phantom_cmd
from userbot import ALIVE_NAME, ALIVE_PIC
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PHANTOM USER"

PHANTOM_VID="https://telegra.ph/file/f6fb42cb5880b47499364.mp4"

if ALIVE_PIC is None:
    ALIVE_PIC=PHANTOM_VID
else:
    ALIVE_PIC=ALIVE_PIC

pm_caption = "**PHANTOM USERBOT IS ONLINE**\n"
pm_caption += f"**My Master** => **{DEFAULTUSER}**\n\n"
pm_caption += "🤖 **SYSTEM INFO** 🤖\n"
pm_caption += "**ᴜsᴇʀʙᴏᴛ - ᴠᴇʀsɪᴏɴ------>> 0.1**\n"
pm_caption += "**ᴛᴇʟᴇᴛʜᴏɴ - ᴠᴇʀsɪᴏɴ ----> 1.15.0**\n"
pm_caption += "**ᴘʏᴛʜᴏɴ -  ᴠᴇʀsɪᴏɴ ------> 3.8.5**\n\n"
pm_caption += "**🌀 SUPPORT INFO 🌀**\n"
pm_caption += "**sᴜᴘᴘᴏʀᴛ - ᴄʜᴀɴɴᴇʟ ---->** [PhantomOt](https://t.me/PhantomOt)\n"
pm_caption += "**sᴜᴘᴘᴏʀᴛ - ɢʀᴏᴜᴘ =** [PhantomSupport](https://t.me/PhantomSupport)\n\n"
pm_caption += f"**[❤️ Create your own PHANTOM USERBOT ❤️](https://dashboard.heroku.com/new?template=https://github.com/prothinkergang/Phantomuserbot)**"

@borg.on(phantom_cmd(pattern=r"me"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
