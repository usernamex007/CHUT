import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "28795512").strip()
API_HASH = os.getenv("API_HASH", "c17e4eb6d994c9892b8a8b6bfea4042a").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7610510597:AAFX2uCDdl48UTOHnIweeCMms25xOKF9PoA").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://iarfggbc:Vxzh_kG7cxa1kHR5faxcd1kuA4R-UT9E@rosie.db.elephantsql.com/iarfggbc").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "SANATANI_TECH")
ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/00eaed55184edf059dbf7.jpg")
LOGGER = os.getenv("LOGGER", "").strip()

if not API_ID:
    raise SystemExit("ɴᴏ ᴀᴘɪ_ɪᴅ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")
elif not API_HASH:
    raise SystemExit("ɴᴏ ᴀᴘɪ_ʜᴀꜱʜ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")
elif not BOT_TOKEN:
    raise SystemExit("ɴᴏ ʙᴏᴛ_ᴛᴏᴋᴇɴ ꜰᴏᴜɴᴅ. ᴇxɪᴛɪɴɢ...")

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("ᴀᴘɪ_ɪᴅ ɪꜱ ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ɪɴᴛᴇɢᴇʀ. ᴇxɪᴛɪɴɢ...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
