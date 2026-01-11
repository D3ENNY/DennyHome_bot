from .main import main

import asyncio, uvloop

#make asyncio faster
uvloop.install() 
asyncio.run(main())