from pyrogram import filters

def register(app):
    
    @app.on_message(filters.command("start"))
    async def start_handler(_, message):
        await message.reply(
            "Bot DennyHome attivato!\n\n"
            "**Lista comandi:**\n"
            "/add_device -> registra nuovo dispositivo\n"
            "/status -> verifica lo stato di un dispositivo\n"
            "/wake -> sfrutta wol per accendere un dispositivo"
        )