# import requests
# import json
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from .. import Anibot, LOGGER, AUTH_USERS
from config import Config
# from kaibot.helping import cmdhelp 
# from ..helpers.search import shorten, anime_query, GRAPHQL
# from ..helpers.other import format_results, conv_to_jpeg

# Start Message
@Anibot.on_message(filters.private & filters.incoming & filters.command("start", prefixes=["/", "."]))
async def start_message(client, message):
    #if message.from_user.id not in Config.AUTH_USERS:
    #     await message.reply_text("Sorry, But Can U Fuck Get Out Of This Bot. U Can't Use This Bot")
    #     return
    await message.reply_photo(
    photo="https://telegra.ph/file/667b8eba8f16e30ba545a.jpg",
    caption = f"Hello [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\nI am an Anime Uploader Bot Working For @Anime_Troop.\n\nI can Search for anime Names And Then Upload To My Masters Required Channel! 😁😁 And other feature s are there but only for my Master",
    parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🙋‍♂️Dev", url="https://t.me/Kai_8_4")],
            [InlineKeyboardButton("Channel", url="https://t.me/Anime_Troop")],
        ],
      )
    )

# Help Message
@Anibot.on_message(filters.private & filters.incoming & filters.command("help", prefixes=["/", "."]))
async def helpmessage(client, message):
    await message.reply_text(
    text=f"Nothin Here. Just a Simple Bot\n\n**Developed From Sratch By @Kai_8_4.**",
    quote=True,
    parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
      [
        [InlineKeyboardButton("🙋‍♂️Dev", url="https://t.me/Kai_8_4")],
        [InlineKeyboardButton("Channel", url="https://t.me/Anime_Troop")],
      ],
    ),
  )

# Anime Command
@Anibot.on_message(filters.private & filters.incoming & filters.command("anime", prefixes=["/", "."]))
async def user_anime(event, message):
    await message.reply_text("Currently Under Work🥲", quote=True, parse_mode="md")

# Broadcast in Channel or Group
@Anibot.on_message(filters.private & filters.incoming & filters.command("post", prefixes=["/", "."]))
async def forward_message(client, message):
    if message.from_user.id in AUTH_USERS:
       if message.reply_to_message is not None:
          post = message.reply_to_message
          await post.forward(Config.CHANNEL_ID)
       #elif " " in message:
       #   post = message.split(" ", 1)[-1]
       #   await post.forward(Config.CHANNEL_ID)
       else:
          await message.reply_text("Bruh, Give Something to Send in Channel!!!")
    else:  
       await message.reply_text("**Sorry, But Can U Fuck Get Out Of This Bot. \n\nU Can't Use This Bot**")
       return


# Process Message
@Anibot.on_message(filters.private & filters.incoming & filters.regex('http'))
async def majnprocess(bot, message):
      uid = message.from_user.id
      uname = message.from_user.first_name
      A = f"[{uname}](tg://user?id={uid}) Choose The Option To Get Get Processed Accordingly."
      if uid not in AUTH_USERS:
           await message.reply_text("**Sorry, But Can U Fuck Get Out Of This Bot. \n\nU Can't Use This Bot**")
           return
      else:
           await message.reply_text(
                 text=A, 
                 reply_to_message_id=message.message_id,
                 reply_markup=InlineKeyboardMarkup(
                       [
                           [InlineKeyboardButton("⚙️Batch⚙️", callback_data="couple_op")],
                       ],
                       [
                           [InlineKeyboardButton("⚙️Single⚙️", callback_data="single_op")],
                       ],
                  ),
             )
