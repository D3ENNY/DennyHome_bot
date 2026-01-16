from pyrogram import filters
import bcrypt

def register(app):
    
    @app.on_message(filters.command("register"))
    async def start_handler(bot, message):
        user_id = message.from_user.id


    def _parse_register_args(msg: str): 
        flags_type = {
            "-u": "user",
            "--user": "user",
            "-pwd": "password",
            "--password": "password"
        }

        parts = msg.split()[1:]
        args = {}
        error = []

        i = 0
        while i < len(parts):
            token = parts[i]

            if token in flags_type:
                if i + 1 >= len(parts) or parts[i + 1] in flags_type:
                    error.append(f"Valore mancante per {token}")
                    i += 1
                    continue

                args[flags_type[token]] = parts[i + 1]
                i += 2
            else:
                i += 1
        
        return args, error

        
    def validate_input(msg: str): 
        if len(msg.split()) == 1: 
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
        required_flags = { "user": ["-u", "--user"], "password": ["-pwd", "--password"] }
        args, error = _parse_register_args(msg)

        for flag_name, aliases in required_flags.items():
            if flag_name not in args and not any(f"Valore mancante per {a}" in error for a in aliases):
                error.append(f"Flag {flag_name} mancante")

        if len(error) > 1: 
            return "\n".join(error)
        return error
                
    def extract_register_data(msg: str):
        args, errors = _parse_register_args(msg)

        if errors: 
            raise ValueError("Input not valid")

        return {
            "user": args["user"],
            "password_hash": bcrypt.hashpw(
                args["password"].encode(),
                bcrypt.gensalt()
            ).decode()
        }