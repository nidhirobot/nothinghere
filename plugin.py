import os

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

from . import *

@ultroid_cmd(
    pattern="unm ?(.*)",
)
async def _(e):
    xx = await eor(e, "`UnGmuting...`")
    if e.reply_to_msg_id:
        userid = (await e.get_reply_message()).sender_id
    elif e.pattern_match.group(1):
        userid = await get_user_id(e.pattern_match.group(1))
    elif e.is_private:
        userid = (await e.get_chat()).id
    else:
        return await eod(xx, "`Reply to some msg or add their id.`", time=5)
    name = (await e.client.get_entity(userid)).first_name
    chats = 0
    async for hurr in e.client.iter_dialogs():
        if hurr.is_group:
            try:
                await e.client.edit_permissions(hurr.id, userid, send_messages=True)
                chats += 1
            except BaseException:
                pass
    ungmute(userid)
    await xx.edit(f"`Ungmuted` [{name}](tg://user?id={userid}) `in {chats} chats.`")
