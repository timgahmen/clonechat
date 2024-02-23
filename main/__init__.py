from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
#API_ID = config("API_ID", default=None, cast=int)
#API_HASH = config("API_HASH", default=None)
#BOT_TOKEN = config("BOT_TOKEN", default=None)
#SESSION = config("SESSION", default=None)
#AUTH = [int(id) for id in config("AUTH", default="").split(",") if id.strip()]

# @Tim_C_1
API_ID = 23736556
API_HASH = "6f2e8cbda3cf92010af144f931f23e44"
# @SRCB_TimC1_Bot
BOT_TOKEN = "6572169169:AAGx3FT74_HU023JkUpX0sM44EJVwQ0ALHQ"
SESSION = "BAFqMOwAoUHMj1mTq5klWAqok_UG_qDHktPalO8ZCjDI6wi35jt4xGg2ulhxwFqVIWn5D34q6VD29e5w9W4dhB2-OrC4T2XJNh4EiQ-AI-NFAYCLf3DO7fKznfR3odMzyEyIv4CnySqHy4N9_0iFttO_RACvWHmosXsZdxdlucvFLO1KDtNwXNiKQLc9Rs0TOzIM-R1KhB8NVQjJCypbGRBgMVXkG62zIajGL7sbgn3fWwCqCu9__2eVNWefokQiGqbTQUZUmic08NGjG_jUlm4AJS-seusZuMMxtpK1kDcVlmyIzfYknDEo4aXw9NSBxaiVFg17h6IJHhekc8T7_snmTc1ZXgAAAAGW5En8AA"

bot = TelegramClient(
    'bot',
    API_ID,
    API_HASH
    ).start(
        bot_token=BOT_TOKEN
        ) 


userbot = Client(
    "user",
    session_string=SESSION,
    api_hash=API_HASH,
    api_id=API_ID
    )

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    #Client.get_me(),
    "user2",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
