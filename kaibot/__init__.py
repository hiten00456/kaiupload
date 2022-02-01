import logging
from .starter import Kai84AnimeBoT
from config import Config

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.getLogger("pyrogram").setLevel(logging.WARNING)

Anibot = Kai84AnimeBoT()
AUTH_URSERS = []
achats = Config.AUTH_USERS.split(" ")
for chats in achats:
    AUTH_USERS.append(int(chats))
