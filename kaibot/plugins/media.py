from ..helpers.progress import progress_for_pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import Config
from .. import Anibot, LOGGER
import os
import zipfile
import time
import glob
import shutil
from pySmartDL import SmartDL
from pyrogram.errors import FloodWait

async def zipprocessfile(bot, message):
     link = message.text
     if url.find("zip"):
        m = await message.reply_text("⚡", reply_to_message_id=message.message_id)
        obj = SmartDL(url, Config.DL_LOCATION)
        obj.start()
        dl_path = obj.get_dest()
        filename = dl_path.split("/")[-1]
        await m.edit_text(f"{filename} Downloaded Successful.\nNow Processing The File", reply_to_message_id=message.message_id)
        LOGGER.info(f"Downloaded in {dl_path}")
        with zipfile.ZipFile(path, 'r') as zip_files:
                contents = zip_files.namelist()
                zip_ref.extractall("downloads")
        dir_name = dl_path.replace(".zip", "")
        constr = ""
        for a in contents:
            b = a.replace(f"{dir_name}/", "")
            constr += b + "\n"
        ans = "**Contents** \n\n" + constr
        if len(ans) > 4096:
            ch = await message.reply_text("Checking Contents for you... \n\nSending as file...")
            f = open("contents.txt", "w+")
            f.write(ans)
            f.close()
            await message.reply_document("contents.txt")
            await ch.delete()
            os.remove("contents.txt")
        else:
            await message.reply_text(ans).
        ok = glob.glob(dir_name/*.[ "mkv", "mp4" ])
        files = [*sorted(ok)]
        for file in files:
               try:
                 start = time.time()
                 check = await msg.reply(f"**⚡Uploading⚡**")
                 LOGGER.info(f"Uploading - {file}")
                 await Anibot.send_document(
                    chat_id=Config.CHANNEL_ID,
                    document=file,
                    caption=f"{file}\n\n**❍ Uploaded By @Anime_Troop**",
                    #thumb=thum,
                    quote=False, 
                    progress=progress_for_pyrogram,
                    progress_args=(bot, check, "🅄🄿🄻🄾🄰🄳🄸🄽🄶", start),
                    disable_notification=False
                  )
               except Exception as e:
                    await message.reply_text(e)
                    
     

            
