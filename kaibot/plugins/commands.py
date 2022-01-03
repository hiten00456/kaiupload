from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from .. import Anibot, LOGGER
from config import Config
from kaibot.helping import cmdhelp 

# Start Message
@Anibot.on_message(filters.private & filters.incoming & filters.command("start", prefixes=["/", "."]))
async def start_message(client, message):
    #if message.from_user.id not in Config.AUTH_USERS:
    #     await message.reply_text("Sorry, But Can U Fuck Get Out Of This Bot. U Can't Use This Bot")
    #     return
    await message.reply_photo(
    photo="https://telegra.ph/file/2d9f8efcacbda9fb72c4e.jpg",
    caption = f"Hello [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\nI am an Anime Uploader Bot Working For @Anime_Troop.\n\nI can Search for anime Names And Then Upload To My Masters Required Channel! 😁😁 And other feature s are there but only for my Master",
    parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Dev", url="https://t.me/Kai_8_4")],
        ],
      )
    )

# Help Message
@Anibot.on_message(filters.private & filters.incoming & filters.command("help", prefixes=["/", "."]))
async def helpmessage(client, message):
    await message.reply_text(
    text=f"{Cmdhelp.HELP_TXT}\n\n**Developed From Sratch By @Kai_8_4.**",
    quote=True,
    parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
      [
        [InlineKeyboardButton("Dev", url="https://t.me/Kai_8_4")],
      ],
    ),
  )

# Anime Command
@Anibot.on_message(filters.private & filters.incoming & filters.command("anime", prefixes=["/", "."]))
async def user_anime(event, message):
   
    if " " in message.text:
        search = message.split(" ", maxsplit=1)[-1]
        ing = await AniBot.send_message(event.chat_id, f"__Searching for__ `{input_str}` __in Anilist__")
        variables = {'search': input_str}
        json = requests.post(GRAPHQL, json={'query': anime_query, 'variables': variables}).json()['data'].get('Media', None)
        if json:
              msg, info, trailer, image = format_results(json)
              if trailer:
                  buttons =[[Button.url("Synopsis", url=info),
                             Button.url("🎆Trailer 🎆", url=trailer)]]
              else:
                  buttons =[[Button.url("Synopsis", url=info)]]
              if image:
                  try:
                       namae = conv_to_jpeg(image)
                       await AnimeBot.send_file(event.chat_id, namae, caption=msg, buttons=buttons, reply_to=event.id, force_document=False)
                       await ing.delete()
                       os.remove(namae)
                   except:
                       msg += f" [\u2063]({image})"
                       await ing.delete()
                       await Anibot.send_message(Config.CHANNEL_ID, msg, buttons=buttons)
    else:
        message.reply_text("Use `/anime `{Query} to get results\nAnd Try to Get the Japanese Name Then the Result will be More Accurate", quote=True, parse_mode="md")

# Broadcast in Channel or Group
@Anibot.on_message(filters.private & filters.incoming & filters.command("post", prefixes=["/", "."]))
async def forward_message(message):
   if message.reply_to_message is not None:
      post = message.reply_to_message
      await post.forward(int(Config.CHANNEL_ID))
   elif " " in me:
      post = message.split(" ", maxsplit=1)[-1]
      await post.forward(int(Config.CHANNEL_ID))
   else:
      return await message.reply_text("Bruh, Give Something to Send in Channel!!!")

        