import os

API_ID = int(os.environ.get("API_ID", 31138834))
API_HASH = os.environ.get("API_HASH", "a6e6098b319618f10693005ee7a77d92")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8551803950:AAEVdjf6EqoAlg21FEaxjQBJx0DrZsiyBak")

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080)) # Default to 8080 if not set

