import asyncio
import websockets

async def test_websocket():
    uri = "wss://a24ea60f-9742-49b2-b5f2-2e7c3e3ace54-00-2dgl6x615ioyh.picard.replit.dev"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, server!")
        response = await websocket.recv()
        print(f"Received message from server: {response}")

asyncio.run(test_websocket())
