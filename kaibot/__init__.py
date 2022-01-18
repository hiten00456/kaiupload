import logging
from .starter import Kai84AnimeBoT

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.getLogger("pyrogram").setLevel(logging.WARNING)

Anibot = Kai84AnimeBoT()
