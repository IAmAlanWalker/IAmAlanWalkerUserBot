
from userbot.utils import admin_cmd
from userbot import CMD_HELP
from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon.tl.functions.photos import DeletePhotosRequest

 
@borg.on(admin_cmd(pattern="deldp ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    
    input_str = event.pattern_match.group(1)
    
    if input_str:
        n = input_str
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=n)))
        await event.edit("photo deletion successful")
    else:
        await event.edit("invalid syntax , use .deldp <count>")
   
        
        
        
CMD_HELP.update({
    "deldp":
    ".deldp (count)\
    \nUsage: Type .deldp (count) this deletes profile photos. \
    "
})            
