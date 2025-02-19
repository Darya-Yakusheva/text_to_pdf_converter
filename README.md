# 📄 Text to PDF Converter Bot
## 👀 Overview

A simple Telegram bot that converts .doc and .docx files into PDFs.\
🚀 **No coding required!** Just use Docker to run the bot in seconds.

---
## 📋 Table of Contents
- [Features](#-features)
- [Quick Start](#-quick-start-for-non-developers)
- [Installation from GitHub](#-advanced-users-for-developers)
- [Running with Docker](#-running-with-docker-for-developers)
- [Additional Notes](#-additional-notes)
- [Feedback & Contributions](#-feedback--contributions)
- [License](#-license)

---
## 📌 Features

✅ Converts .doc and .docx files to .pdf\
✅ Supports files up to **20MB**\
✅ Runs inside a **Docker container** (no need to install Python)\
✅ Uses **environment variables** for secure configuration

---
## 🚦 Quick Start (For Non-Developers)

If you just want to use the bot **without coding**, follow these steps:
### 1️⃣ Install Docker

Download and install [Docker](https://www.docker.com/).
### 2️⃣ Create a Telegram Bot
[Create](https://core.telegram.org/bots/features#creating-a-new-bot) your own Telegram bot using [BotFather](https://t.me/botfather).
### 3️⃣ Create a .env file
In the folder where you'll run the bot, create a **.env** file and add your [Telegram bot token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) there:

`TELEGRAM_BOT_TOKEN=your_bot_token_here`

### 4️⃣ Run the Bot

Once the .env file is ready, start the bot by running:
```bash
docker run --env-file .env iakusheva/text_to_pdf_converter_bot
```

🎉 **That’s it!** Your bot is now running. 🚀\
Send it a .doc or .docx file in Telegram, and it will return a .pdf.

---
## 🧑‍💻 Advanced Users (For Developers)

If you want to modify the bot’s code, follow these steps:
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Darya-Yakusheva/text_to_pdf_converter
cd text_to_pdf_converter
```
### 2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**👨‍💻 Now you can make all necessary changes in the source code.**
### 4️⃣ Set Up Environment Variables

Create a **.env** file in the project directory and add your [Telegram bot token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) there:
`TELEGRAM_BOT_TOKEN=your_bot_token_here`\
Replace `your_bot_token_here` with your actual token from [BotFather](https://t.me/botfather).
### Notes:
Ensure you have LibreOffice installed if running locally. See installation steps below:

#### Installing LibreOffice:

- #### Ubuntu / Debian:
```bash
sudo apt update && sudo apt install -y libreoffice
```
- #### MacOS (using Homebrew):
```
brew install --cask libreoffice
```
- #### Windows:
  - Download the installer from [LibreOffice official site](https://www.libreoffice.org/download/download-libreoffice/).
  - Run the installer and follow the on-screen instructions.

### 5️⃣ Run the Bot Locally
```bash
python -m app.converter_tg_bot
```

---
## 🐳 Running with Docker (For Developers)

If you prefer using Docker, follow these steps after [downloading the source code](#Clone the Repository) and [creating a .env file](#Set Up Environment Variables):
### 1️⃣ Build the Docker Image
If you plan to **modify** the bot’s code, you need to **build** the image locally instead of using the public one:
```bash
docker build -t text_to_pdf_converter_bot .
```
**⚒️ Remember to rebuild your image after every modification of the code**
### 2️⃣ Run the Container
```bash
docker run --env-file .env text_to_pdf_converter_bot
```
### 3️⃣ Check Running Containers
To ensure your bot is running:
```bash
docker ps
```
### 4️⃣ Stopping the Bot
To stop the bot **without deleting the container**, find the **Container ID** from docker ps and run:
```bash
docker stop <container_id>
```
🎉 **That’s it!** Now your bot is running inside a Docker container. 🚀

---
## 📝 Additional Notes
- **Ensure LibreOffice is installed** if running the bot locally.
- **Docker image includes LibreOffice** by default.
- **Bug Reports & Contributions:** Open an issue or submit a PR on GitHub.

**🚀 Happy converting!**

---
## 📨 Feedback & Contributions

If you find a **bug**, **mistake**, or have a **suggestion**, you can report it in one of the following ways:

1️⃣ [GitHub Issues](https://github.com/Darya-Yakusheva/text_to_pdf_converter/issues) – Open an issue describing the problem or feature request.\
2️⃣ **Fork & Pull Request** – If you want to **fix** something yourself:
- Fork the repository
- Make your changes
- Submit a pull request (PR)

3️⃣ **Contact Me** – If you prefer, feel free to [reach out](https://www.linkedin.com/in/daria-iakusheva/) directly.

**Your feedback is highly appreciated! 😊**

---
## 📜 License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).