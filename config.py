import os


#I will Add Later The .env System
#import dotenv
# dotenv.load_dotenv()

class Config(object):
  AUTH_USERS = os.environ.get("AUTH_USERS")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "2030766680:AAEBO6Slyd3RCeaCQKwlUXXCtmZkdi3BbTc")
  API_ID = int(os.environ.get("API_ID", 3509841))
  API_HASH = os.environ.get("API_HASH", "68a5f01af74e8ef888458fdaea3376eb")
  THUMBNAIL = os.environ.get("THUMBNAIL_URL", "https://telegra.ph/file/5bb45f4b5255252a67c07.jpg")
  CHANNEL_ID = int(os.environ.get("UPLOAD_CH_ID", -1001447866756))
  DL_LOCATION = "./downloads"
