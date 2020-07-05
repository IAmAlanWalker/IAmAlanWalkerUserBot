"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

from userbot import AUTONAME

from userbot import ALIVE_NAME


DEFAULTUSER = str(AUTONAME) if AUTONAME else "@Sensible_userbot"

@borg.on(admin_cmd(pattern=r"deploy"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

   # input_str = event.pattern_match.group(1)



    await event.edit("Deploying...")

    animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (SensibleUserbot/Sensibleerbot)**",
            "**Build started by user** **{DEFAULTUSER}**",
            "**Deploy** `535a74f0` **by user** **{DEFAULTUSER}**",
            "**Restarting Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from starting to up**",
            "__INFO:Sensible Userbot:Logged in as {DEFAULTUSER}",
            "__INFO:Sensible Userbot:Successfully loaded all plugins__ Userbot By @ceowhitehatcracks Join @sensible_userbot For Learning How To Deploy",
            "**Build Succeeded Userbot By @ceowhitehatcracks Join @sensible_userbot For Learning How To Deploy**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
