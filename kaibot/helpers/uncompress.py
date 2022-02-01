from .. import Anibot, LOGGER
from config import Config
import os, time
import shutil

import zipfile, rarfile, tarfile


async def zipp(bot, com, msg, dl_path):
    filename = dl_path.split("/")[-1]
    sm = await msg.reply(f"`{filename}` Downloaded Successfully in {tt}.")
    with zipfile.ZipFile(dl_path, 'r') as zipObj:
        zipObj.extractall("downloads")
        dir_name = dl_path.replace(".zip", "")
    if not os.path.exists(dir_name):
        await sm.edit("Got Some Error while extracting")
        return
    else:
        st = await msg.reply("Processed The File Now Uploading Will Start Soon")
        pass
    ok = os.listdir(dir_name)
    c = 0
    for list in ok:
       if list == "desktop.ini":
           try:
              os.remove(f"{dir_name}/desktop.ini")
           except:
              pass
       elif os.path.isdir(os.path.join(dir_name, list)):
           shutil.rmtree(os.path.join(dir_name, list))
       else:
           c += 1
    countt = await msg.reply_text(f"Found {c} files to upload")
    files = []
    for file in ok:
        file = os.path.join(dir_name, file)
        files.append(file)
    files.sort()
    thum = "thumb.jpeg"
    await countt.delete()
    for file in files:
          try:
             start = time.time()
             filenamelist = file.split("/")[-1]
             channelmsg = await Anibot.send_message(chat_id=Config.CHANNEL_ID, text=f"Uploading - `{filenamelist}`")
             check = await msg.reply(f"Uploading - `{filenamelist}`")
            # LOGGER.info(f"Uploading - {file}")
             await Anibot.send_document(
                 chat_id=Config.CHANNEL_ID,
                 document=file,
                 caption=f"◎ `{filenamelist}`\n\n**⌬ Uploaded By @Anime_Troop**",
                 thumb=thum,
                 force_document=True,
                 progress=progress_for_pyrogram,
                 progress_args=(bot, check, "🅄🄿🄻🄾🄰🄳🄸🄽🄶", start)
             )
             time.sleep(2)
             await channelmsg.delete()
             await chech.delete()
          except FloodWait as e:
             time.sleep(e.x)
    complete=await msg.reply("Completed The Task. Now Taking a Sleep Nap", quote=True)
    time.sleep(6)
    await complete.edit("Completed `{filename}` Task For You")



