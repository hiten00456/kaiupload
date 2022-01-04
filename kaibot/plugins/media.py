from ..helpers.progress import progres_for_pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import Config
from .. import LOGGER
import os
import zipfile
import time
import glob
import shutil
from pySmartDL import SmartDL
from pyrogram.errors import FloodWait

async def zipprocessfile(message):
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
            await message.reply(ans)
            await con_message.delete()
        # extracted_files = [i async for i in absolute_paths(dir_name)]
            fileExtensions = [ "mkv", "mp4" ]
            listOfFiles    = []
