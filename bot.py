from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from prediction import generate_predictions, hot_numbers, cold_numbers
from scraper import get_latest_result

TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Kerala Lottery AI Bot Ready!"
    )

async def result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_latest_result()
    await update.message.reply_text(
        f"Latest Result:\n{data['result']}\nDate: {data['date']}"
    )

async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    preds = generate_predictions()
    text = "Today's Predictions:\n\n"
    text += "\n".join(preds)

    await update.message.reply_text(text)

async def hot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nums = hot_numbers()
    await update.message.reply_text(f"Hot Numbers: {nums}")

async def cold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nums = cold_numbers()
    await update.message.reply_text(f"Cold Numbers: {nums}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("result", result))
app.add_handler(CommandHandler("guess", guess))
app.add_handler(CommandHandler("hot", hot))
app.add_handler(CommandHandler("cold", cold))

print("Bot Running...")
app.run_polling()