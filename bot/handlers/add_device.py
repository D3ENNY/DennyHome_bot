from pyrogram import filters

def register(app):
    
    @app.on_message(filters.command("add_device"))
    async def start_handler(_, message):
        await message.reply(

        )