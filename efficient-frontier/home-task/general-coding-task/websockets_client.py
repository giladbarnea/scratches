import asyncio
import websockets
import sys
from pprint import pprint as pp, pformat as pf
import websocket

async def local():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        
        await websocket.send(name)
        print(f"> {name}")
        
        greeting = await websocket.recv()
        print(f"< {greeting}")


ftx = 'wss://ftx.com/ws/options/trades'
bitmex = 'wss://testnet.bitmex.com/realtime?subscribe=execution:XBTUSD,instrument'


async def main(url):
    async with websockets.connect(url) as ws:
        # name = input("What's your name? ")
        
        # await ws.send(name)
        # print(f"> {name}")
        reader = ws.reader
        res = await ws.recv()
        print(f'res: ({type(res)})')
        print(res)


asyncio.run(main(sys.argv[1]))
