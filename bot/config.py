import os
from dotenv import local_dotenv

load_doatenv()

class config: 
    API_ID = int(os.getenv("API_ID",0))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
config=config()