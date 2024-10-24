# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9253184"))
API_HASH = getenv("API_HASH", "d431225b58df7ca994ec12248743a1aa")
BOT_TOKEN = getenv("BOT_TOKEN", "7162171355:AAFmVMQvLcLOenU19nXCFCZd5HfUm66yvqA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6173241744").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
