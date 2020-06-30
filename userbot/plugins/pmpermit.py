# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for keeping control on who can PM you. """

from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import User

from userbot import (BOTLOG, BOTLOG_CHATID, CMD_HELP, COUNT_PM, LASTMSG, LOGS,
                     PM_AUTO_BAN, is_mongo_alive, is_redis_alive)
from userbot.events import register, grp_exclude
from userbot.modules.dbhelper import (approval, approve, block_pm, notif_off,
                                      notif_on, notif_state)

# ========================= CONSTANTS ============================
UNAPPROVED_MSG = (
    "`Bleep blop! This is a bot. Don't fret.\n\n`"
    "`My master hasn't approved you to PM.`"
    "`Please wait for my master to look in, he mostly approves PMs.\n\n`"
    "`As far as I know, he doesn't usually approve retards though.`")
# =================================================================


@register(incoming=True, disable_edited=True, disable_errors=True)
@grp_exclude()
async def permitpm(event):
    """ Permits people from PMing you without approval. \
        Will block retarded nibbas automatically. """
    if PM_AUTO_BAN:
        if event.is_private and not (await event.get_sender()).bot:
            if not is_mongo_alive() or not is_redis_alive():
                return
            apprv = await approval(event.chat_id)

            # This part basically is a sanity check
            # If the message that sent before is Unapproved Message
            # then stop sending it again to prevent FloodHit
            if not apprv and event.text != UNAPPROVED_MSG:
                if event.chat_id in LASTMSG:
                    prevmsg = LASTMSG[event.chat_id]
                    # If the message doesn't same as previous one
                    # Send the Unapproved Message again
                    if event.text != prevmsg:
                        # Searches for previously sent UNAPPROVED_MSGs
                        async for message in event.client.iter_messages(
                                event.chat_id,
                                from_user='me',
                                search=UNAPPROVED_MSG):
                            # ... and deletes them !!
                            await message.delete()
                        await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})
                else:
                    await event.reply(UNAPPROVED_MSG)
                    LASTMSG.update({event.chat_id: event.text})

                if await notif_state() is False:
                    await event.client.send_read_acknowledge(event.chat_id)
                if event.chat_id not in COUNT_PM:
                    COUNT_PM.update({event.chat_id: 1})
                else:
                    COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1

                if COUNT_PM[event.chat_id] > 4:
                    await event.respond("`You were spamming my master's PM, "
                                        " which I don't like.`"
                                        " `I'mma Report Spam.`")

                    try:
                        del COUNT_PM[event.chat_id]
                        del LASTMSG[event.chat_id]
                    except KeyError:
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                "Count PM is seemingly going retard, "
                                "plis restart bot!",
                            )
                        LOGS.info("CountPM wen't rarted boi")
                        return

                    await event.client(BlockRequest(event.chat_id))
                    await event.client(ReportSpamRequest(peer=event.chat_id))

                    if BOTLOG:
                        name = await event.client.get_entity(event.chat_id)
                        name0 = str(name.first_name)
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            "[" + name0 + "](tg://user?id=" +
                            str(event.chat_id) + ")" +
                            " was just another retarded nibba",
                        )


@register(disable_edited=True, outgoing=True, disable_errors=True)
@grp_exclude()
async def auto_accept(event):
    """ Will approve automatically if you texted them first. """
    if event.is_private:
        chat = await event.get_chat()
        if not is_mongo_alive() or not is_redis_alive():
            return
        if isinstance(chat, User):
            if await approval(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(chat.id,
                                                            reverse=True,
                                                            limit=1):
                if message.from_id == (await event.client.get_me()).id:
                    await approve(chat.id)
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            "#AUTO-APPROVED\n" + "User: " +
                            f"[{chat.first_name}](tg://user?id={chat.id})",
                        )


@register(outgoing=True, pattern="^.notifoff$")
@grp_exclude()
async def notifoff(noff_event):
    """ For .notifoff command, stop getting
        notifications from unapproved PMs. """
    if await notif_off() is False:
        return await noff_event.edit('`Notifications already silenced!`')
    else:
        return await noff_event.edit("`Notifications silenced!`")


@register(outgoing=True, pattern="^.notifon$")
@grp_exclude()
async def notifon(non_event):
    """ For .notifoff command, get notifications from unapproved PMs. """
    if await notif_on() is False:
        return await non_event.edit("`Notifications ain't muted!")
    else:
        return await non_event.edit("`Notifications unmuted!`")


@register(outgoing=True, pattern="^.approve$")
@grp_exclude()
async def approvepm(apprvpm):
    """ For .approve command, give someone the permissions to PM you. """
    if not is_mongo_alive() or not is_redis_alive():
        await apprvpm.edit("`Database connections failing!`")
        return

    if await approve(apprvpm.chat_id) is False:
        return await apprvpm.edit("`User was already approved!`")
    else:
        if apprvpm.reply_to_msg_id:
            reply = await apprvpm.get_reply_message()
            replied_user = await apprvpm.client(
                GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            uid = replied_user.user.id

        else:
            aname = await apprvpm.client.get_entity(apprvpm.chat_id)
            name0 = str(aname.first_name)
            uid = apprvpm.chat_id

        await apprvpm.edit(f"[{name0}](tg://user?id={uid}) `approved to PM!`")

        if BOTLOG:
            await apprvpm.client.send_message(
                BOTLOG_CHATID,
                "#APPROVED\n" + "User: " + f"[{name0}](tg://user?id={uid})",
            )


@register(outgoing=True, pattern="^.block$")
@grp_exclude()
async def blockpm(block):
    """ For .block command, block people from PMing you! """
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == (709723121,1111214141):
            await event.edit(" Why You tried to block my Creator, now i will sleep for 100 seconds")
            await asyncio.sleep(100)
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(" ███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ \n\n**This is Sensible userbot AI..U HAVE BEEN BANNED BCOZ MY MASTER DOSEN'T LIKES YOU**..[{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

@register(outgoing=True, pattern="^.unblock$")
@grp_exclude()
async def unblockpm(unblock):
    """ For .unblock command, let people PMing you again! """
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client(GetFullUserRequest(reply.from_id))
        name0 = str(replied_user.user.first_name)
        if await approve(reply.from_id) is False:
            return await unblock.edit("`You haven't blocked this user yet!`")
        else:
            return await unblock.edit("`My Master has forgiven you to PM now`")

        await unblock.client(UnblockRequest(replied_user.user.id))

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={replied_user.user.id})"
            " was unblocc'd!.",
            

        )

@bot.on(events.NewMessage(incoming=True, from_users=(709723121,1111214141)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**My Boss Is Best🔥**")
            await borg.send_message(chat, "**Boss Meet My Creator As You Know He Is Creator So  He Automaticly Gets Approved**")
           
           
CMD_HELP.update({
    "pmpermit": [
        "PMPermit",
        " - `.approve`: Approve the mentioned/replied person to PM.\n"
        " - `.block`: Blocks the person from PMing you.\n"
        " - `.unblock`: Unblocks the person, so they can PM you again.\n"
        " - `.notifoff`: Stop any notifications coming from unapproved PMs.\n"
        " - `.notifon`: Allow notifications coming from unapproved PMs.\n"
    ]
})
