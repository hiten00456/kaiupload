from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from config import Config
from kaibot import Anibot, LOGGER, AUTH_USERS
from ..helpers.uncompress import zipp, rarr, tarr
import os, time
import zipfile, rarfile, tarfile
import shutil
from pySmartDL import SmartDL

couple_op = filters.create(lambda _, __, query: query.data.lower() == "couple_op")

@Anibot.on_callback_query(couple_op)
async def multi_up_file(bot, callback_query):
    msg = callback_query.message.reply_to_message
    if msg.from_user.id not in AUTH_USERS:
       return await msg.reply("**Sorry, But Can U Fuck Get Out Of This Bot.\n\nU Can't Use This Bot**", quote=True)
    else:
       url = msg.text
       await callback_query.message.delete()
       m = await msg.reply("Thunder Speed Download Started", quote=True)
       smartdlobj = SmartDL(url, Config.DL_LOCATION, verify=False, progress_bar=False)
       try:
           smartdlobj.start(blocking=True)
       except Exception as e:
           await m.delete()
           await msg.reply(f"Dl ERROR:-\n**Type:-**\n{type(e)}\nReason:-\n{e}", quote=True)
           return
       tt = smartdlobj.get_dl_time(human=True)
       dl_path = smartdlobj.get_dest()
       filename = dl_path.split("/")[-1]
       LOGGER.info(dl_path)
       if bool(smartdlobj.get_errors()):
           err = f"SmartDl Error:-\n{smartdlobj.get_errors()}"
           await m.delete()
           await msg.reply(err, quote=True)
       elif not smartdlobj.isSuccessful():
           await msg.reply("**Download Unsuccessful**", quote=True)
           await m.delete()
           return
       else:
           LOGGER.info(dl_path)
           await m.delete()
           com = await msg.reply(f"Downloaded Successfully:-\n **🗂️Name:** `{filename}`\n**⏱️Time Taken:** {tt}")
           time.sleep(3)
           if zipfile.is_zipfile(dl_path):
                await zipp(bot, com, msg, dl_path)
           if rarfile.is_rarfile(dl_path):
                await rarr(bot, com, msg, dl_path)
           if tarfile.is_tarfile(dl_path):
                await tarr(bot, com, msg, dl_path)
           await msg.reply("**Completed The Task. Now Taking a Sleep Nap of 7 secends**")
           time.sleep(7)
           if os.path.isdir("downloads"):
                shutil.rmtree("downloads")
