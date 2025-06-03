import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

VAULT_CHANNEL_ID = int(os.getenv("VAULT_CHANNEL_ID", "-1002624785490"))  # Channel ID to fetch videos from
FORCE_JOIN_CHANNEL = os.getenv("FORCE_JOIN_CHANNEL", "bot_backup")       # Must join channel username

ADMIN_USER_ID = int(os.getenv("ADMIN_USER_ID", "7755789304"))  # Owner Telegram ID

# MongoDB connection URI (set in Heroku config vars)
MONGO_URI = os.getenv("MONGO_URI")

WELCOME_IMAGE = "https://files.catbox.moe/19j4mc.jpg"

DEVELOPER_LINK = "https://t.me/unbornvillian"
SUPPORT_LINK = "https://t.me/botmine_tech"
TERMS_LINK = "https://t.me/bot_backup/7"

COOLDOWN_SECONDS = 8
