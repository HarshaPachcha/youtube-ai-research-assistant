# main.py

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_TOKEN
from transcript import get_transcript
from summarizer import generate_summary
from qa_engine import answer_question
from rag_engine import chunk_transcript

sessions = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to YouTube AI Research Assistant!\n"
        "Send a YouTube link to begin.\n"
        "Use /language Hindi to switch language."
    )


async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/language English\n/language Hindi"
        )
        return

    language = context.args[0].capitalize()

    if language not in ["English", "Hindi"]:
        await update.message.reply_text("Supported: English, Hindi")
        return

    if user_id not in sessions:
        sessions[user_id] = {}

    sessions[user_id]["language"] = language

    await update.message.reply_text(f"✅ Language set to {language}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        text = update.message.text

        # Preserve existing language
        language = "English"
        if user_id in sessions and "language" in sessions[user_id]:
            language = sessions[user_id]["language"]

        # YouTube Link
        if "youtube.com" in text or "youtu.be" in text:

            await update.message.reply_text("⏳ Fetching transcript...")

            transcript_data = get_transcript(text)

            if not transcript_data:
                await update.message.reply_text("❌ Transcript not available.")
                return

            chunks = chunk_transcript(transcript_data)

            sessions[user_id] = {
                "video_id": text,
                "transcript": transcript_data,
                "chunks": chunks,
                "language": language
            }

            await update.message.reply_text("🧠 Generating summary...")

            summary = generate_summary(transcript_data, language)
            await update.message.reply_text(summary)
            return

        # Question
        if user_id not in sessions:
            await update.message.reply_text("⚠ Send a YouTube link first.")
            return

        await update.message.reply_text("🤖 Thinking...")

        session = sessions[user_id]
        chunks = session["chunks"]
        language = session.get("language", "English")

        answer = answer_question(chunks, text, language)
        await update.message.reply_text(answer)

    except Exception as e:
        print("ERROR:", e)
        await update.message.reply_text("⚠ Internal error occurred.")


if __name__ == "__main__":
    print("🚀 Starting bot...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("language", set_language))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot is running...")
    app.run_polling()