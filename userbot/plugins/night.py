"""AFK Plugin for Sensible_userbot
Syntax: .night """
import asyncio
import datetime
from telethon import events
from telethon.tl import functions, types
from userbot.utils import admin_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
USER_AFK = {}
afk_time = None
last_afk_message = {}


@borg.on(admin_cmd(pattern=r"night "))


            
            msg = None
        message_to_reply = f"Important Notice**\n\n[This User Is Sleeping On The Bed ...](https://telegra.ph/file/3e6d2fb965f293e3680ff.jpg)** " + \
            f"\n\n__ I'll back in a few Light years__\n**REASON**: {reason}" \
            if reason \
            else f"**Important Notice**\n\n[This User Is Sleeping On The Bed ...](https://telegra.ph/file/3e6d2fb965f293e3680ff.jpg) "
        msg = await event.reply(message_to_reply)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602
            )
     

