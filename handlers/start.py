from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from config import *
from database import is_banned, log_event
from telegram.error import BadRequest

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uid = user.id

    if await is_banned(uid):
        await update.message.reply_text("🚫 You are banned from using this bot.")
        return

    try:
        member = await context.bot.get_chat_member(FORCE_JOIN_CHANNEL, uid)
        if member.status in ["left", "kicked"]:
            join_button = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Join Channel", url=f"https://t.me/{FORCE_JOIN_CHANNEL}")]]
            )
            await update.message.reply_text(
                "🚫 You must join our channel to use this bot.\nPlease join and then try again.",
                reply_markup=join_button,
            )
            return
    except BadRequest:
        pass

    log_text = (
        f"📥 New User Started Bot\n\n"
        f"👤 Name: {user.full_name}\n"
        f"🆔 ID: {user.id}\n"
        f"📛 Username: @{user.username if user.username else 'N/A'}"
    )
    await log_event(log_text)

    bot_name = (await context.bot.get_me()).first_name
    caption = (
        f"🥵 Welcome to {bot_name}!\n"
        "Here you will access the most unseen videos.\n👇 Tap below to explore:"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📩 Get Random Video", callback_data="get_video")],
        [InlineKeyboardButton("Developer", url=DEVELOPER_LINK)],
        [
            InlineKeyboardButton("Support", url=SUPPORT_LINK),
            InlineKeyboardButton("Help", callback_data="show_privacy_info"),
        ],
    ])

    await update.message.reply_photo(
        photo=WELCOME_IMAGE,
        caption=caption,
        reply_markup=keyboard,
    )

    disclaimer = (
        "⚠️ **Disclaimer** ⚠️\n\n"
        "We do NOT produce or spread adult content.\n"
        "This bot is only for forwarding files.\n"
        "If videos are adult, we take no responsibility.\n"
        "Please read terms and conditions."
    )
    await context.bot.send_message(
        chat_id=uid,
        text=disclaimer,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("📘 Terms & Conditions", url=TERMS_LINK)]]
        ),
        parse_mode="Markdown",
      )
