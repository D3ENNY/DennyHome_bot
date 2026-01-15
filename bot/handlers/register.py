from pyrogram import filters

def register(app):
    
    @app.on_message(filters.command("register"))
    async def start_handler(bot, message):
        await bot.send_message(message.chat.id, validate_input(message.text))   

        
    def validate_input(msg: str): 
        if len(msg.split(" ")) == 1: 
            return (
                "**NAME:** register\n\n"
                "**DESCRIPTION:**\n"
                "This is a command that allows you to register a new user to the bot.\n\n"
                "**FLAG:**\n"
                "`-u`,   `--user`       Nickname of the user\n"
                "`-pwd`, `--password`   Password of the user\n\n"
                "**USAGE:**\n"
                "/register -u USERNAME -pwd MYPASSWORD"
            )
        
        flags_type = {
            "-u": "user",
            "--user": "user",
            "-pwd": "password",
            "--password": "password"
        }

        required_flags = {
            "user": ["-u", "--user"],
            "password": ["-pwd", "--password"]
        }
        parts = msg.split(" ")[1:]

        found = set()
        error = []
        i = 0

        while i < len(parts):
            token = parts[i]

            if token in flags_type:

                if i + 1 >= len(parts):
                    error.append(f"Valore mancante per {token}")
                    i += 1
                    continue

                if parts[i + 1] in flags_type:
                    error.append(f"Valore mancante per {token}")
                    i += 1
                    continue

                found.add(flags_type[token])
                i += 2
            else:
                i += 1

        for flag_name, aliases in required_flags.items():
            if flag_name not in found and not any(f"Valore mancante per {a}" in error for a in aliases):
                error.append(f"Flag {flag_name} mancante")

        if len(error) > 1: 
            return "\n".join(error)
        else: 
            return error
                
            

###
#args = dict(zip(parts[::2], parts[1::2]))
#print(args)
###