from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_USER_ID, VAULT_CHANNEL_ID
from database import add_video
from telegram.error import BadRequest

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Only process messages from vault channel
    if update.effective_chat.id != VAULT_CHANNEL_ID:
        return

    msg = update.effective_message

    # Only process videos (or video files)
    if msg.video or msg.document or msg.video_note:
        try:
            await add_video(msg.message_id)
        except Exception as e:
            print(f"Error adding video to DB: {e}")
