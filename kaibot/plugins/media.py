from ..helpers.progress import progress_for_pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import Config
from .. import Anibot, LOGGER
import os
import zipfile36 as zipfile
import time
import glob
import shutil
from pySmartDL import SmartDL
from pyrogram.errors import FloodWait

async def zipprocessfile(bot, message):
     url = message.text
     if url.find("zip"):
        m = await message.reply_text("⚡", reply_to_message_id=message.message_id)
        obj = SmartDL(url, Config.DL_LOCATION)
        obj.start()
        dl_path = obj.get_dest()
        filename = dl_path.split("/")[-1]
        if not os.path.exists("extracted"):
            os.mkdir("extracted")
        else:
            pass
        await m.edit_text(f"{filename} Downloaded Successful.\nNow Processing The File", reply_to_message_id=message.message_id)
        LOGGER.info(f"Downloaded in {dl_path}")
        with zipfile.ZipFile(path, 'r') as zip_files:
                contents = zip_files.namelist()
                zip_ref.extractall("extracted")
        dir_name = dl_path.replace(f"/downloads/{filename}", f"/extracted/{filename}")
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
            await message.reply_text(ans)
        ok = []
        for ext in ('*.mp4', '*.mkv'):
             ok.extend(glob.glob(os.path.join(dir_name, ext)))
        #ok = glob.glob('*.mkv') + glob.glob('*.mp4')
        files = ok.sort()
        thum = "thumb.jpeg"
        for file in files:
               try:
                 start = time.time()
                 check = await Anibot.send_text(chat_id=Config.CHANNEL_ID, text="Uploading New Anime")
                 LOGGER.info(f"Uploading - {file}")
                 await Anibot.send_document(
                    chat_id=Config.CHANNEL_ID,
                    document=file,
                    caption=f"◎`{file}`\n\n**⌬ Uploaded By @Anime_Troop**",
                    thumb=thum,
                    force_document=True,
                    quote=False, 
                    progress=progress_for_pyrogram,
                    progress_args=(bot, check, "🅄🄿🄻🄾🄰🄳🄸🄽🄶", start),
                    disable_notification=False
                  )
               except FloodWait as e:
                  time.sleep(e.x)
        await message.reply_text("Completed The Task. Now Taking a Sleep Nap")
        time.sleep(7)
        if os.path.isdir("downloads"):
                 shutil.rmtree("downloads")
            if os.path.isdir("extracted"):
                 shutil.rmtree("extracted")
     else:
        return await message.reply_text("This Is Not A Zip File. \nSend A Link Which Has zip in the url in it.", reply_to_message_id=message.message_id)      
