import os

API_ID = int(os.environ.get("API_ID", "15529802"))
API_HASH = os.environ.get("API_HASH", "92bcb6aa798a6f1feadbc917fccb54d3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8348307399:AAH7Wnci84CVEECBtFurF6MZOxMrZJN4vwM")

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://RENDERTEST:RENDERTEST@cluster0.5mowi1z.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "SilentXBotz")

WEB_SERVER = os.environ.get("WEB_SERVER", "True").lower() in ("true", "1", "t")
PORT = int(os.environ.get("PORT", "8080"))
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))

TG_WORKERS = int(os.environ.get("TG_WORKERS", "4"))

# Your Koyeb/Heroku App Url
# Example : https://yorappurl.koyeb.app/
APP_URL = os.environ.get("APP_URL", None)
