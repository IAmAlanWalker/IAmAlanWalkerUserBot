# For @UniBorg

# Courtesy @yasirsiddiqui

"""

.leave

"""



from telethon.tl.functions.channels import LeaveChannelRequest

from userbot.utils import admin_cmd

import time





@borg.on(admin_cmd("bye", outgoing=True))

async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("`Yahan Pagalpan ho rha h Mai aur nahi seh skta!`")

        time.sleep(3)

        if '-' in str(e.chat_id):

            await borg(LeaveChannelRequest(e.chat_id))

        else:

            await e.edit('`Oppps, Sir This is Not A Chat`')
