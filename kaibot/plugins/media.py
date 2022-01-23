from ..helpers.progress import progress_for_pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from config import Config
from .. import Anibot, LOGGER
import os
import zipfile
import time
import glob
import shutil
from pySmartDL import SmartDL
from pyrogram.errors import FloodWait

process_filter = filters.create(lambda _, __, query: query.data.lower() == "summer")

@Client.on_callback_query(process_filter)
async def zipprocessfile(bot, callback_query):
     main = callback_query.message.reply_to_message
     url = main.text
     await callback_query.message.delete()
     if url.find("zip"):
        m = await callback_query.message.reply("Downloading...", quote=True)
        obj = SmartDL(url, Config.DL_LOCATION, progress_bar=False)
        obj.start()
        tt = obj.get_dl_time(human=True)
        dl_path = obj.get_dest()
        filename = dl_path.split("/")[-1]
        LOGGER.info(dl_path)
        await m.delete()
        sm = await callback_query.message.reply_text(f"`{filename}` Downloaded Successfully in {tt}.\n**Now Processing The File**")
        LOGGER.info(f"Downloaded in {dl_path}")
        with zipfile.ZipFile(dl_path, 'r') as zipObj:
                zipObj.extractall("downloads")
                dir_name = dl_path.replace(".zip", "")
        if not os.path.exists(dir_name):
             await callback_query.message.reply_text("Got Some Error while extracting")
             await sm.delete()
             return
        else:
             pass
        constr = os.listdir(dir_name)
        count = 0
        for list in constr:
             if list == "desktop.ini":
                 os.remove(f"{dir_name}/{list}")
                 count -= 1
             elif os.path.isdir(os.path.join(dir_name, list)):
                 shutil.rmtree(os.path.join(dir_name, list))
                 count -= 1
             else:
                 count += 1
        countt = await callback_query.message.reply_text(f"Found {count} files to upload")
        ok = os.listdir(dir_name)
        files = []
        for file in ok:
              file = os.path.join(dir_name, file)
              files.append(file)
        files.sort()
        thum = "thumb.jpeg"
        for file in files:
               try:
                 start = time.time()
                 filenamelist = file.split("/")[-1]
                 chech = await Anibot.send_message(chat_id=Config.CHANNEL_ID, text=f"Uploading - `{filenamelist}`")
                 check = await callback_query.message.reply(f"Uploading - `{filenamelist}`")
                 # LOGGER.info(f"Uploading - {file}")
                 await Anibot.send_document(
                    chat_id=Config.CHANNEL_ID,
                    document=file,
                    caption=f"◎`{filenamelist}`\n\n**⌬ Uploaded By @Anime_Troop**",
                    thumb=thum,
                    force_document=True,
                    progress=progress_for_pyrogram,
                    progress_args=(bot, check, "⚡🅄🄿🄻🄾🄰🄳🄸🄽🄶⚡", start)
                  )
                 await check.delete()
                 await chech.delete()
               except FloodWait as e:
                  time.sleep(e.x)
        await countt.delete()
        await sm.delete()
        com = await callback_query.message.reply_text("Completed The Task. Now Taking a Sleep Nap")
        time.sleep(7)
        if os.path.isdir("downloads"):
              shutil.rmtree("downloads")
     else:
        await callback_query.message.reply_text("This Is Not A Zip File. \nSend A Link Which Has zip in the url in it.", reply_to_message_id=callback_query.message.message_id)
        return      
