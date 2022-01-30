# (c) @CRACKERON

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, event: Message):
    """
    Custom Pyrogram Based Telegram Bot's Force Subscribe Function by @CRACKERON.
    If User is not Joined Force Sub Channel Bot to Send a Message & ask him to Join First.
    
    :param bot: Pass Client.
    :param event: Pass Message.
    :return: It will return 200 if Successfully Got User in Force Sub Channel and 400 if Found that User Not Participant in Force Sub Channel or User is Kicked from Force Sub Channel it will return 400. Also it returns 200 if Unable to Find Channel.
    """
    
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Uɴʙʟᴇ Tᴏ Fᴏʀᴄᴇ Sᴜʙᴄʀɪʙᴇ{Config.UPDATES_CHANNEL}\n\nError: {err}\n\nContact Support Group: https://t.me/TeleRoid14")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=event.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=event.from_user.id,
                text="Sorry Sir,Sᴏʀʀʏ Uɴᴋɪʟʟ , Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Usᴇ Wɪᴛʜ ᴍᴇ🥵.",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=event.from_user.id,
            text="**⚡Hᴇʏ Jᴏɪɴ Mʏ Mᴋ Bᴏᴛs Tᴏ Usᴇ Mᴇ , Oʀ Gᴇᴛ Oᴜᴛ Bʟᴀᴄᴋsʜᴇᴇᴘ 🌬️",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Jᴏɪɴ Oɴ Mᴋ Bᴏᴛs🤹", url=invite_link.invite_link)
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=event.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ Uɴᴀʙʟᴇ Tᴏ Fᴏʀᴄᴇ Sᴜʙ\nError: {err}\n\nContact Support Group: https://t.me/TeleRoid14")
        return 200
