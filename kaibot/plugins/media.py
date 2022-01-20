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
     url = callback_query.message.reply_to_message
     await callback_query.message.delete()
     if url.find("zip"):
        m = await callback_query.message.reply("Downloading...", quote=True)
        obj = SmartDL(url, Config.DL_LOCATION, progress_bar=False)
        obj.start()
        tt = obj.get_dl_time(human=True)
        dl_path = obj.get_dest()
        LOGGER.info(dl_path)
        filename = dl_path.split("/")[-1]
        await m.delete()
        sm = await callback_query.message.reply_text(f"`{filename}` Downloaded Successful in {tt}.\n**Now Processing The File**")
        LOGGER.info(f"Downloaded in {dl_path}")
        with zipfile.ZipFile(dl_path, 'r') as zip_files:
                zip_files.extractall("downloads")
        dir_name = dl_path.replace(".zip", "")
        constr = os.listdir(dir_name)
        count = 0
        for list in constr:
             count += 1
        countt = await callback_query.message.reply_text(f"Found {count} files to upload")
        #ok = []
        #for ext in ('*.mp4', '*.mkv'):
        #     ok.extend(glob.glob(os.path.join(dir_name, ext)))
        ok = glob.glob(f"{dir_name}/*.mkv")
        files = [*sorted(ok)]
        #files = ok.sort()
        thum = "thumb.jpeg"
        for file in files:
               try:
                 start = time.time()
                 check = await Anibot.send_text(chat_id=Config.CHANNEL_ID, text=f"Uploading {file}")
                 LOGGER.info(f"Uploading - {file}")
                 await Anibot.send_document(
                    chat_id=Config.CHANNEL_ID,
                    document=file,
                    caption=f"◎`{file}`\n\n**⌬ Uploaded By @Anime_Troop**",
                    thumb=thum,
                    force_document=True,
                    quote=True, 
                    progress=progress_for_pyrogram,
                    progress_args=(bot, check, "🅄🄿🄻🄾🄰🄳🄸🄽🄶", start),
                    disable_notification=False
                  )
               except FloodWait as e:
                  time.sleep(e.x)
        await countt.delete()
        await sm.delete()
        com =await callback_query.message.reply_text("Completed The Task. Now Taking a Sleep Nap")
        time.sleep(5)
        await com.delete()
        if os.path.isdir("downloads"):
              shutil.rmtree("downloads")
     else:
        await callback_query.message.reply_text("This Is Not A Zip File. \nSend A Link Which Has zip in the url in it.", reply_to_message_id=callback_query.message.message_id)
        return      
