#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24068031
API_HASH = "620e80fbc06cff9e5c9a4912d8e61ba0"
BOT_TOKEN = "7656706291:AAEk9X0CITRU6rRDsA8-o1_gvrAv4869xPs"
SESSION = "BQFvP78AT-pJ-vIhN2UcfYejQRjOEBxVVKIHFHqzuq-kq7OM6HNNcc1NgGbYTBpyeEthPEe9eqOyy97KPPPD00jd9ZzIYahVFM3QnGYvyu8EaFmJPeLFmOwZsW-f1vSa-aVFzpS6ovbnaN25Wfgnjr74u5U5E2qwvLR6poiioqu3FA_POXWaMoSDb-0ubrwgn5NHd2SdLFyoh-0yVPFaCExLJmIdQBQXmOBU7CPBHoV7Z4SR8OnNuB869wzBiqoQ9Z0dlMo2O7avJl6k2SxZvm1XENDNFLThoLAF9KqLZ-xQBL8xv9wtEdpLBsFUaSX3IqdPaiqa_4iLtv3oiSshnNQ4H7TI9AAAAAFrL8EnAA"
FORCESUB = "tech_tipsbd"
AUTH = "6091906014"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
