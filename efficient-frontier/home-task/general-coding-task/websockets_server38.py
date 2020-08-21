# %%
import asyncio
import websockets


# %%


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    
    greeting = f"Hello {name}!"
    
    await websocket.send(greeting)
    print(f"> {greeting}")


# %%
async def main():
    start_server: websockets.server.Serve = websockets.serve(hello, "localhost", 8765)
    server: websockets.server.WebSocketServer = await start_server
    await asyncio.sleep(1000)
    return server


# %%
result = asyncio.run(main())
# %%
print(result)
