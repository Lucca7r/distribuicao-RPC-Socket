import asyncio
import websockets
import base64
import xmlrpc.client

connected = set()

async def preto_e_branco(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            # Criar uma conexão RPC
            with xmlrpc.client.ServerProxy("https://dddddc04-f2f9-4153-ae32-0172e5096b6f-00-gqgkds7g0wct.spock.replit.dev:8000/") as proxy:
                # Chamar a função RPC para converter a imagem para preto e branco
                imagem_pb_base64 = proxy.preto_e_branco(message)

            await websocket.send(imagem_pb_base64)
    finally:
        connected.remove(websocket)

start_server = websockets.serve(preto_e_branco, "0.0.0.0", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()