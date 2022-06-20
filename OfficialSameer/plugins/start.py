import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import SAM, SAM2, SAM3, SAM4, SAM5, SAM6, SAM7, SAM8, SAM9, SAM10, ALIVE_PIC, OWNER_ID

DEADLY_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/e0fad27744428f1460d5c.jpg"

Deadly_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Anime_Gaming_chat_global")
        ],
        [
        Button.url("• ᴄᴍᴅs •", "https://telegra.ph/%F0%9D%97%A5%F0%9D%97%9C%F0%9D%97%AD%F0%9D%97%A2%F0%9D%97%98%F0%9D%97%9F-%F0%9D%97%AB-%F0%9D%97%A6%F0%9D%97%A3%F0%9D%97%94%F0%9D%97%A0-11-28-2")
        ]
        ]
               
DeadlyX_Button = [
        [
        Button.url("𝙈𝙪𝙨𝙞𝙘 𝘽𝙤𝙩 𝄞", "https://t.me/Schwi_Musicbot"),
        Button.url("𝘼𝙁𝙆 𝘽𝙤𝙩 ♡", "https://t.me/C2_Probot")
        ],
        [
            InlineKeyboardButton(text="💕", url=f"https://t.me/Miss_Jibril"),
            InlineKeyboardButton(text="♥️", url=f"https://t.me/Miss_STEPHANIEE"),
            InlineKeyboardButton(text="🦊", url=f"https://t.me/Miss_Izuna"),
            InlineKeyboardButton(text="🔮", url=f"https://t.me/Miss_FIEL"),
            InlineKeyboardButton(text="🍒", url=f"https://t.me/Miss_Shiro"),
        ],
        [
            InlineKeyboardButton(text="💕", url=f"https://t.me/Miss_Jibril"),
            InlineKeyboardButton(text="♥️", url=f"https://t.me/Miss_STEPHANIEE"),
            InlineKeyboardButton(text="🦊", url=f"https://t.me/Miss_Izuna"),
            InlineKeyboardButton(text="🔮", url=f"https://t.me/Miss_FIEL"),
            InlineKeyboardButton(text="🍒", url=f"https://t.me/Miss_Shiro"),
        ],
        [
        Button.url("𝘼𝙣𝙞𝙢𝙚 𝘾𝙝𝙖𝙩 𝙂𝙧𝙤𝙪𝙥", "https://t.me/+LuNfF7pzIggyNWE1"),
        ],
        [
        Button.url("𝐎𝐰𝐧𝐞𝐫", "https://t.me/Lord_DSP_3")
        ]
        ]
        
        
#USERS 


@SAM.on(events.NewMessage(pattern="/start"))
@SAM2.on(events.NewMessage(pattern="/start"))
@SAM3.on(events.NewMessage(pattern="/start"))
@SAM4.on(events.NewMessage(pattern="/start"))
@SAM5.on(events.NewMessage(pattern="/start"))
@SAM6.on(events.NewMessage(pattern="/start"))
@SAM7.on(events.NewMessage(pattern="/start"))
@SAM7.on(events.NewMessage(pattern="/start"))
@SAM8.on(events.NewMessage(pattern="/start"))
@SAM9.on(events.NewMessage(pattern="/start"))
@SAM10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DeadlyBot = await event.client.get_me()
       bot_id = DeadlyBot.first_name
       bot_username = DeadlyBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheDeadly = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n** @Lord_dsPRObot 🎋.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=ownermsg, 
                  buttons=Deadly_Button)
       else:
            await event.client.send_file(TheDeadly,
                  DEADLY_IMG,
                  caption=usermsg, 
                  buttons=DeadlyX_Button)
                
