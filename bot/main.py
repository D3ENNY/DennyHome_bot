from pyrogram.client import Client
from bot.config import config

from bot.handlers import start, add_device, wake, status

async def main():
    app = Client(
        "DennyHome_Bot",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN
    )
    
    await app.start()
    
    # Handler setup
    start.register(app)
    add_device.register(app)
    wake.register(app)
    status.register(app)
    
    print("Bot started. Press Ctrl+C to stop")
    
    
    try:
        await asyncio.Event().wait() 
    finally:
        await app.stop()