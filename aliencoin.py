from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# تنظیمات لاگینگ
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: CallbackContext) -> None:
    try:
        photo_path = r'C:\Users\USER\Downloads\Telegram Desktop\photo_2024-07-20_19-49-19.jpg'  # مسیر فایل عکس

        # ارسال عکس با متن توضیحی
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(photo_path, 'rb'),
            caption='سلام خوش آمدی! این اپ برای تبادل نظر و تبلیغات رایگان و به حقیقت رساندن ایده‌هایتان با کمک دوستانی که پیدا می‌کنید ساخته شده است. برای شروع، دکمه (/play) را بزنید.'
        )
    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text('مشکلی در ارسال عکس یا پیام پیش آمد.')

async def play(update: Update, context: CallbackContext) -> None:
    # ایجاد دکمه شیشه‌ای برای نمایش وب اپ
    web_app_url = 'https://yourusername.github.io/products.html'  # آدرس URL وب اپ شما
    keyboard = [
        [InlineKeyboardButton("شروع وب اپ", url=web_app_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text('برای شروع وب اپ، روی دکمه زیر کلیک کنید:', reply_markup=reply_markup)

def error_handler(update: Update, context: CallbackContext) -> None:
    logging.error(f"Update {update} caused error {context.error}")

def main() -> None:
    # جایگزین کردن توکن واقعی ربات خود به جای 'YOUR_ACTUAL_BOT_TOKEN'
    application = Application.builder().token('7265876197:AAFmdW761tcYxweQ5VRUrgmdULiHKRkxgtk').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    application.add_error_handler(error_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
