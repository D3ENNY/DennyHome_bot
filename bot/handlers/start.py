from pyrogram import filters

def register(app):
    
    @app.on_message(filters.command("start"))
    async def start_handler(_, message):
        await message.reply(
            "Bot DennyHome attivato!\n"
            "**Lista comandi:**"
            "/add_device -> registra nuovo dispositivo"
            "/status -> verifica lo stato di un dispositivo"
            "/wake -> sfritta wol per accendere un dispositivo"
        )