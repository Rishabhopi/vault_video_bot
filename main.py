import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import BOT_TOKEN, ADMIN_USER_ID, VAULT_CHANNEL_ID
from handlers.start import start
from handlers.callbacks import back_to_start, callback_get_video
from handlers.admin import add_sudo_command, remove_sudo_command, ban_command, unban_command, broadcast_command
from handlers.uploader import handle_channel_post

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Command Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("addsudo", add_sudo_command))
app.add_handler(CommandHandler("remsudo", remove_sudo_command))
app.add_handler(CommandHandler("ban", ban_command))
app.add_handler(CommandHandler("unban", unban_command))
app.add_handler(CommandHandler("broadcast", broadcast_command))

# CallbackQuery Handlers
app.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_to_start$"))
app.add_handler(CallbackQueryHandler(callback_get_video, pattern="^get_video$"))

# Channel posts handler (only for vault channel)
app.add_handler(MessageHandler(filters.Chat(VAULT_CHANNEL_ID) & (filters.VIDEO | filters.Document.ALL | filters.VIDEO_NOTE), handle_channel_post))

print("Bot is starting...")
app.run_polling()
