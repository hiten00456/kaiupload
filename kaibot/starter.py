import asyncio
import logging
from os import path
from config import Config
from pyrogram import (
  Client, 
  idle
)

class FFclient(Client):
    def __init__(self):
        Kai().__init__(
            "Kai84AnimeBoT",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workdir="./",
            plugins=dict(root="kaibot.plugins")
        )
        bot_info = None

    async def __run(self):
        await Kai().start()
        self.bot_info  = await self.get_me()
        logging.info(f"@{self.bot_info.username} Is Working Now")
        await idle()
    
    def run(self):
        asyncio.get_event_loop().run_until_complete(self.__run()
