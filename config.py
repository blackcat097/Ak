# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_USERNAME = getenv("OWNER_USERNAME", "Abishnoi1M")
BOT_USERNAME = getenv("BOT_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Abishnoi_bots")
BOT_NAME = getenv("BOT_NAME","Abishnoi 🥀")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/2c3097ae03f950800a66f.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1452219013").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/KingAbishnoi/Ak")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "Abishnoi")
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
