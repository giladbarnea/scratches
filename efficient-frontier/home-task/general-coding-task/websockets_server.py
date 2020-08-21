import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    
    greeting = f"Hello {name}!"
    
    await websocket.send(greeting)
    print(f"> {greeting}")


start_server: websockets.server.Serve = websockets.serve(hello, "localhost", 8765)
loop = asyncio.get_event_loop()
server: websockets.server.WebSocketServer = loop.run_until_complete(start_server)
loop.run_forever()
