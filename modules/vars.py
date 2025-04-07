import os

API_ID    = os.environ.get("API_ID", "22215080")
API_HASH  = os.environ.get("API_HASH", "6ab80ad5d78fee18fdd9b909edfbafd5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7684348611:AAGLdg08V_V4321WKWP_g-r3O5QiCgUGIM0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
