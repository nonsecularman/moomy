#
# AloneMusic Config (FINAL STABLE FIX)
#

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ================= BASIC ================= #

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 8106551502))

# ================= LIMIT ================= #

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# ================= LOGGER ================= #

LOGGER_ID = int(getenv("LOGGER_ID", 0))

# ✅ REQUIRED (error fix)
DEBUG_IGNORE_LOG = []

# ================= ADS ================= #

ADS_MODE = getenv("ADS_MODE", None)

# ================= API ================= #

API_URL = getenv("API_URL", "https://api.thequickearn.xyz")
VIDEO_API_URL = getenv(
    "VIDEO_API_URL",
    "https://api.video.thequickearn.xyz"
)
API_KEY = getenv("API_KEY", "NxGBNexGenBotsb5ccdf")

# ================= HEROKU ================= #

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/nonsecular/Fix"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ================= SUPPORT ================= #

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/iscamz"
)

SUPPORT_CHAT = getenv(
    "SUPPORT_CHAT",
    "https://t.me/kryshupdate"
)

AUTO_LEAVING_ASSISTANT = bool(
    getenv("AUTO_LEAVING_ASSISTANT", None)
)

# ================= SPOTIFY ================= #

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# ================= PLAYLIST ================= #

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# ================= FILE LIMIT ================= #

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600)
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824)
)

# ================= STRING SESSION ================= #

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# ================= GLOBAL ================= #

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ================= START MEDIA ================= #

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://files.catbox.moe/lvtd1a.jpg"
)

# ✅ future video support
START_VIDEO_URL = getenv(
    "START_VIDEO_URL",
    "https://files.catbox.moe/qviplg.mp4"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/4ansts.jpg"
)

PLAYLIST_IMG_URL = "https://files.catbox.moe/419n5s.jpg"
STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://files.catbox.moe/ztfuxp.jpg"
)

TELEGRAM_AUDIO_URL = "https://files.catbox.moe/419n5s.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/419n5s.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/419n5s.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/419n5s.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/419n5s.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/419n5s.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/419n5s.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/419n5s.jpg"

# ================= UTILS ================= #

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i
        for i, x in enumerate(reversed(stringt.split(":")))
    )

DURATION_LIMIT = int(
    time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
)

# ================= URL CHECK ================= #

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )
