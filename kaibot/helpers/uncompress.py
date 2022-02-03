from ..helpers.progress import progress_for_pyrogram
from pyrogram.types import Message
from .. import Anibot, LOGGER
from config import Config
import os, time
import shutil
import zipfile, rarfile, tarfile
from pyrogram.errors import FloodWait



# Zip Process
async def zipp(bot, com, msg, dl_path):
    filename=dl_path.split("/")[-1]
    sm = await msg.reply("Processing The File For U", quote=True)
    with zipfile.ZipFile(dl_path, 'r') as zipObj:
        zipObj.extractall("downloads")
        dir_name = dl_path.replace(".zip", "")
    if not os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        await sm.edit("Got Some Error while extracting")
        return
    else:
        await sm.delete()
        st = await msg.reply("Processed The File Now Uploading Will Start Soon")
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
    await st.delete()
    ok = os.listdir(dir_name).sort()
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
             check = await msg.reply(f"Uploading - {filenamelist}", quote=True)
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
             await check.delete()
          except FloodWait as e:
             time.sleep(e.x)
    complete=await msg.reply("Completed The Task. Now Taking a Sleep Nap", quote=True)
    time.sleep(6)
    await complete.edit(f"Completed `{filename}` Task For You")

# Tar Process
async def tarr(bot, com, msg, dl_path):
    filename=dl_path.split("/")[-1]
    sm = await msg.reply("Processing The File", quote=True)
    with tarfile.TarFile(dl_path, 'r') as tarObj:
        tarObj.extractall("downloads")
        dir_name = dl_path.replace(".tar", "")
    if not os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        await sm.edit("Got Some Error while extracting")
        return
    else:
        await sm.delete()
        st = await msg.reply("Processed The File Now Uploading Will Start Soon")
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
    countt = await msg.reply(f"Found {c} files to upload")
    ok = os.listdir(dir_name).sort()
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
             check = await msg.reply(f"Uploading - {filenamelist}", quote=True)
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
             await check.delete()
          except FloodWait as e:
             time.sleep(e.x)
    complete=await msg.reply("Completed The Task. Now Taking a Sleep Nap", quote=True)
    time.sleep(6)
    await complete.edit(f"Completed `{filename}` Task For You")

# Rar Process
async def rarr(bot, com, msg, dl_path):
    filename=dl_path.split("/")[-1]
    sm = await msg.reply("Processing The File", quote=True)
    with rarfile.RarFile(dl_path, 'r') as rarObj:
        rarObj.extractall("downloads")
        dir_name = dl_path.replace(".rar", "")
    if not os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        await sm.edit("Got Some Error while extracting")
        return
    else:
        await sm.delete()
        st = await msg.reply("Processed The File Now Uploading Will Start Soon")
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
    await st.delete()
    countt = await msg.reply_text(f"Found {c} files to upload")
    ok = os.listdir(dir_name).sort()
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
             check = await msg.reply(f"Uploading - {filenamelist}", quote=True)
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
             await check.delete()
          except FloodWait as e:
             time.sleep(e.x)
    complete=await msg.reply("Completed The Task. Now Taking a Sleep Nap", quote=True)
    time.sleep(6)
    await complete.edit(f"Completed `{filename}` Task For You")
