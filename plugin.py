from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *

@ultroid_cmd(pattern="https$")
async def _(event):
    if event.fwd_from:
        return
    chat = "@hqproxy_bot"
    msg = await eor(event, "Sending Your Https Proxies...")
    async with ultroid_bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1683047947)
            )
            await conv.send_message("/https")
            response = await response
        except YouBlockedUserError:
            await msg.edit("Boss! Please Unblock @hqproxy_bot ")
            return
        if response.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless ðŸ˜‚ðŸ˜‚")
        else: 
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)
