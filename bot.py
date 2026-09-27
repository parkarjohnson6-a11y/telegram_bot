import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

CHANNEL_URL = "https://t.me/addlist/PepJQUTEOoQ4MzZk"
PHOTO_FILE = "photo_id.txt"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "JOIN & GET GOLD VIP CHANNEL FREE 👑⚡", url=CHANNEL_URL
                )
            ]
        ]
    )

    caption = "🔥 GOLD VIP SIGNAL CHANNEL FREE! 🔥\n\nDaily 95%+ Accuracy Signals!\nJoin now for free access 👇"

    if os.path.exists(PHOTO_FILE):
        with open(PHOTO_FILE, "r") as f:
            photo_id = f.read().strip()
        await update.message.reply_photo(
            photo=photo_id, caption=caption, reply_markup=keyboard
        )
    else:
        await update.message.reply_text(caption, reply_markup=keyboard)


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.photo:
        photo_id = update.message.photo[-1].file_id
        with open(PHOTO_FILE, "w") as f:
            f.write(photo_id)
        await update.message.reply_text("Image saved successfully!")


def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN environment variable not set.")
        return

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
