import asyncio
import uvloop

# Make asyncio faster
uvloop.install()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

from .main import main

if __name__ == "__main__":
    asyncio.run(main())