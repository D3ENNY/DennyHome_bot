from pyrogram import filters

def register(app):
    
    @app.on_message(filters.command("login"))
    async def start_handler(_, message):
        await message.reply(

        )

###
#   verified = bcrypt.checkpw(
#       "PASSWORD".encode(),
#       data["password_hash"].encode(), 
#   )
###        verified = bcrypt.checkpw(
            "PASSWORD".encode(),
            data["password_hash"].encode(), 
        )