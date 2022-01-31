from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from config import Config
from .. import Anibot, LOGGER, AUTH_URSERS
from ..helpers.uncompress import zipp, rarr, tarr
import os
import zipfile, rarfile, tarfile
import shutil
from pySmartDL import SmartDL

cuple_op = filters.create(lambda _, __, query: query.data.lower() == "couple_op")

@Anibot.on_callback_query(couple_op)
async def multi_up_file(bot, callback_query):
    msg = callback_query.message.reply_to_message
    if msg.from_user.id is not in AUTH_URSERS:
       return await msg.reply("**Sorry, But Can U Fuck Get Out Of This Bot.\n\nU Can't Use This Bot**", quote=True)
    else:
       url = main.text
       await callback_query.message.delete()
       m = await callback_query.message.reply("Downloading...", quote=True)
       smartdlobj = SmartDL(url, Config.DL_LOCATION, verify=False, progress_bar=False)
          try:
              smartdlobj.start(blocking=True)
          except Exception as e:
              await m.delete()
              await msg.reply(f"Dl ERROR:-\n**Type:-**\n{type(e)}\nReason:-\n{e}", quote=True)
              return
       tt = obj.get_dl_time(human=True)
       dl_path = obj.get_dest()
       LOGGER.info(dl_path)
       if bool(smartdlobj.get_errors()):
           err = "SmartDl Error:-\n" + smartdlobj.get_errors()
           await m.delete()
           await msg.reply(err, quote=True)
       elif not smartdlobj.isSuccessful():
           await msg.reply("**Download Unsuccessful**", quote=True)
           await m.delete()
           return
       else:
           LOGGER.info(dl_path)
           com = await m.edit(f"**Downloaded Successfully {filename} in {tt}")
           time.sleep(2)
           if zipfile.is_zipfile(dl_path):
                await zipp(bot, com, msg, dl_path)
           if rarfile.is_rarfile(dl_path):
                await rarr(bot, com, msg, dl_path)
           if tarfile.is_tarfile(dl_path):
                await tarr(bot, com, msg, dl_path)
           com = await callback_query.message.reply_text("**Completed The Task. Now Taking a Sleep Nap of 7 secends**")
           time.sleep(7)
           if os.path.isdir("downloads"):
                shutil.rmtree("downloads")
