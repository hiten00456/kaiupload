from ..helpers.progress import progress_for_pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from config import Config
from kaibot import Anibot, LOGGER, AUTH_USERS
import os
import zipfile
import time
import glob
import shutil
from pySmartDL import SmartDL
from pyrogram.errors import FloodWait

single_op = filters.create(lambda _, __, query: query.data.lower() == "single_op")

@Client.on_callback_query(single_op)
async def single_up_file(bot, callback_query):
     msg = callback_query.message.reply_to_message
     if msg.from_user.id not in AUTH_USERS:
        await msg.reply("**Sorry, But Can U Fuck Get Out Of This Bot.\n\nU Can't Use This Bot**", quote=True)
     else:
        url = msg.text
        await callback_query.message.delete()
        m = await msg.reply("𝚃𝚑𝚞𝚗𝚍𝚎𝚛𝚒𝚗𝚐 𝚃𝚑𝚎 𝙻𝚒𝚗𝚔⚙️", quote=True)
        smartdlobj = SmartDL(url, Config.DL_LOCATION, verify=False, progress_bar=False)
        try:
           smartdlobj.start(blocking=True)
        except Exception as e:
           etype = type(e)
           await m.delete()
           await msg.reply(f"Dl ERROR:-\n**Type:-**\n{etype}\nReason:-\n{e}")
           return
        tt = smartdlobj.get_dl_time(human=True)
        dl_path = smartdlobj.get_dest()
        if bool(smartdlobj.get_errors()):
           err = "SmartDl Error:-\n" + smartdlobj.get_errors()
           await m.delete()
           await msg.reply(err, quote=True)
        elif not smartdlobj.isSuccessful():
           await msg.reply("**Download Unsuccessful**", quote=True)
           await m.delete()
           return
        else:
           filename = dl_path.split("/")[-1]
           LOGGER.info(dl_path)
           com = await m.edit(f"**Downloaded Successfully {filename} in {tt}")
           time.sleep(2)
           thum="thumb.jpeg"
           try:
               start = time.time()
               chech = await Anibot.send_message(chat_id=Config.CHANNEL_ID, text=f"Uploading - `{filename}`")
               check = await msg.reply(f"Uploading - `{filename}`")
               #LOGGER.info(f"Uploading - {filename}")
               await Anibot.send_document(
                  chat_id=Config.CHANNEL_ID,
                  document=dl_path,
                  caption=f"◎`{filename}`\n\n**⌬ Uploaded By @Anime_Troop**",
                  thumb=thum,
                  force_document=True,
                  progress=progress_for_pyrogram,
                  progress_args=(bot, check, "⚡🅄🄿🄻🄾🄰🄳🄸🄽🄶⚡", start)
                )
               time.sleep(2)
               await check.delete()
               await chech.delete()
           except FloodWait as e:
                  time.sleep(e.x)
           await com.delete()
           
