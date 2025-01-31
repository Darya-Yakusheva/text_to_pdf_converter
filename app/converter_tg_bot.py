import os
from tempfile import TemporaryDirectory

from dotenv import load_dotenv
from converter import convert_file
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()  # Load environment variables from .env file

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
START_MESSAGE = (
    "Send me a .doc or .docx file and I will convert it "
    "into a .pdf and send back to you.\n\n"
    "I can only download files of up to 20MB in size."
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command sent by a user.
    Sends a message to the user explaining the bot's functionality.

    Parameters:
        update (Update): Incoming update from the Telegram bot API.
                         Contains details about the user's message.
        context (ContextTypes.DEFAULT_TYPE): Context object
                                             containing bot-related data.

    Returns:
        None
    """

    await update.message.reply_text(START_MESSAGE)


async def reply_to_non_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles unrecognized messages sent by the user.
    Informs the user that the bot only supports file conversion.

    Parameters:
        update (Update): Incoming update from the Telegram bot API.
                         Contains details about the user's message.
        context (ContextTypes.DEFAULT_TYPE): Context object
                                             containing bot-related data.

    Returns:
        None
    """
    message = (
        "I'm just a simple file converter bot "
        "and cannot process what you've sent me.\n\n"
        f"{START_MESSAGE}"
    )
    await update.message.reply_text(message)


async def get_input_file_info(update: Update) -> tuple[str, str]:
    """
    Extracts the file ID and name from the received document.

    Parameters:
        update (Update): Incoming update from the Telegram bot API.

    Returns:
        tuple[str, str]: The file ID and original file name.
    """
    input_file_info = update.message.document
    return input_file_info.file_id, input_file_info.file_name


async def download_file(context: ContextTypes.DEFAULT_TYPE, file_id: str, save_path: str) -> str:
    """
    Downloads the file from Telegram and saves it locally.

    Parameters:
        context (ContextTypes.DEFAULT_TYPE): Context object
                                             containing bot-related data.
        file_id (str): Unique identifier for the file to download.
        save_path (str): Path where the file should be saved.

    Returns:
        str: The path to the saved file.
    """
    input_file = await context.bot.get_file(file_id)
    return await input_file.download_to_drive(save_path)


async def convert_and_send_file(update: Update, saved_file: str, tempdirname: str) -> None:
    """
    Converts the downloaded file to PDF and sends it back to the user.

    Parameters:
        update (Update): Incoming update from the Telegram bot API.
        saved_file (str): Path to the downloaded file.
        tempdirname (str): Temporary directory for processing files.

    Returns:
        None
    """
    try:
        converted_file = convert_file(saved_file, tempdirname)
        await update.message.reply_text(
            "Sending you the converted file.\n\n"
            "Please note that the original file name might be "
            "slightly modified due to Telegram bot limitations."
        )
        await update.message.reply_document(converted_file)
    except Exception as e:
        await update.message.reply_text(
            f"An error occurred while processing the file:\n{e}"
        )


async def file_handling(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles incoming document files sent by the user.
    Downloads the file, converts it to PDF,
    and sends the converted file back to the user.

    Parameters:
        update (Update): Incoming update from the Telegram bot API.
                         Contains details about the user's
                         message and attached document.
        context (ContextTypes.DEFAULT_TYPE): Context object
                                             containing bot-related data.

    Returns:
        None
    """
    input_file_id, input_file_name = await get_input_file_info(update)

    try:
        # Use TemporaryDirectory to handle file storage and cleanup
        with TemporaryDirectory() as tempdirname:
            # Download the file and save it to the temporary directory
            saved_file = await download_file(
                context, input_file_id, os.path.join(tempdirname, input_file_name)
            )
            # Convert and send the converted file back to the use
            await convert_and_send_file(update, saved_file, tempdirname)
    except Exception as e:
        await update.message.reply_text(
            f"An error occurred while downloading the file "
            f"{input_file_name}:\n{e}"
        )


def main():
    # Create the application instance with the bot token
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command and message handlers for the bot
    # Handles /start command
    app.add_handler(CommandHandler("start", start))
    # Handles non-document
    app.add_handler(MessageHandler(~filters.Document.ALL, reply_to_non_document))
    # Handles document files
    app.add_handler(MessageHandler(filters.Document.ALL, file_handling))

    # Start the bot and keep polling for new updates
    print("Bot launched!")
    app.run_polling()


if __name__ == "__main__":
    main()
