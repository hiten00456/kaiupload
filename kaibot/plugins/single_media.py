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

# process_filter = filters.create(lambda _, __, query: query.data.lower() == "summer")

@Client.on_callback_query()
async def zipprocessfile(bot, callback_query):
     # Rewrite All
