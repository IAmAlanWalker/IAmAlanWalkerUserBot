"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`█   ▄▀█ █▀▄▀█   ▄▀█ █░░ █ █░█ █▀▀   █▀▄▀█ █▄█   █▀▄▀█ ▄▀█ █▀ ▀█▀ █▀▀ █▀█ \n █   █▀█ █░▀░█   █▀█ █▄▄ █ ▀▄▀ ██▄   █░▀░█ ░█░   █░▀░█ █▀█ ▄█ ░█░ ██▄ █▀▄"
                     "\n Success usually comes to those who are too busy to be looking for it👍ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍʏ ᴍᴀꜱᴛᴇʀ🎈🎈`**\n\n"
                     "**✅Telethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**✅Bot Made By:- @Ceowhitehatcracks \nCo Owner ꌚꀤꈤ ꏳꂦꀷꏂ @sin_code\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**"
                     "**✅Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n💞Always with you, my peru master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "[Deploy this userbot Now](https://github.com/spandey112/SensibleUserbot)")
