from pyrogram import Client
from bot.config import config

from bot.handlers import start, register, wake, status

async def main():
    app = Client(
        "DennyHome_Bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        api_token=config.BOT_TOKEN
    )
    
    # Handler setup
    start.register(app)
    register.register(app)
    wake.register(app)
    status.register(app)