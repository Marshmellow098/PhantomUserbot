# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

PHANTOM_VID="https://telegra.ph/file/f6fb42cb5880b47499364.mp4"

ALIVE_PIC = os.environ.get("ALIVE_PIC" , None)

if ALIVE_PIC is None:
    ALIVE_PIC=PHANTOM_VID
else:
    ALIVE_PIC=ALIVE_PIC

pm_caption = "**PHANTOM USERBOT IS ONLINE**\n"
pm_caption += f"**My Master** => {DEFAULTUSER}\n\n"
pm_caption += "🤖 **SYSTEM INFO** 🤖\n"
pm_caption += "**ᴛᴇʟᴇᴛʜᴏɴ - ᴠᴇʀsɪᴏɴ ----> **15.0.0\n"
pm_caption += "**ᴘʏᴛʜᴏɴ -  ᴠᴇʀsɪᴏɴ ------> **3.8.5\n\n"
pm_caption += "**🌀 SUPPORT INFO 🌀**\n"
pm_caption += "**sᴜᴘᴘᴏʀᴛ - ᴄʜᴀɴɴᴇʟ ---->** [PhantomOt](https://t.me/PhantomOt)\n"
pm_caption += "**sᴜᴘᴘᴏʀᴛ - ɢʀᴏᴜᴘ =** [PhantomSupport](https://t.me/PhantomSupport)\n\n"
pm_caption += f"**[❤️ Create your own Phantom Userbot ❤️](https://dashboard.heroku.com/new?template=https://github.com/prothinkergang/Phantomuserbot)**"

@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
