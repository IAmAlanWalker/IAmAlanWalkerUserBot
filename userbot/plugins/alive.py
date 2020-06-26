"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
pm_caption = "` Bot Made By @CeoWhiteHatCracks \n"
pm_caption += "`Team Members Of This bot @spkal01 @sin_code @blackhathacker7 @MrJetex\n"
pm_caption += "`Sensible Userbot IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**Sensible Userbot OS** : `3.14`\n"
pm_caption += "**Current Sat** : `Ceo White Hat Cracks `\n\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n\n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "[Deploy Sensible Userbot Made By @CEowhitehatcracks](https://github.com/spandey112/SensibleUserbot)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
