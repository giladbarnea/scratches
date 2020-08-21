import asyncio
import socket
import urllib.parse
import sys

ftx = 'wss://ftx.com/ws/options/trades'
bitmex = 'wss://testnet.bitmex.com/realtime?subscribe=execution:XBTUSD,instrument'


async def wait_for_data():
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()
    
    # Create a pair of connected sockets.
    rsock, wsock = socket.socketpair()
    
    # Register the open socket to wait for data.
    reader, writer = await asyncio.open_connection(sock=rsock)
    
    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())
    
    # Wait for data
    data = await reader.read(100)
    
    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()
    
    # Close the second socket
    wsock.close()


async def foo(url):
    loop = asyncio.get_running_loop()
    split = urllib.parse.urlsplit(url)
    print(f'split url: (hostname: {split.hostname})', split)
    # reader, writer = await asyncio.open_connection(split.hostname)
    reader, writer = await asyncio.open_connection(url)
    print('opened connection')
    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')
    writer.close()
    await writer.wait_closed()


# asyncio.run(foo(sys.argv[1]))
asyncio.run(wait_for_data())
