import asyncio
import websockets
import base64
from xmlrpc.client import ServerProxy
import logging

connected = set()
logging.basicConfig(level=logging.DEBUG)


async def preto_e_branco(websocket, path):
  logging.debug('Nova conexão estabelecida')
  connected.add(websocket)
  try:
    async for message in websocket:
      url_servidor = 'dddddc04-f2f9-4153-ae32-0172e5096b6f-00-gqgkds7g0wct.spock.replit.dev'
      servidor = ServerProxy(f'https://{url_servidor}:8000')
      
      resposta = servidor.preto_branco(message)

      await websocket.send(resposta)
  finally:
    logging.debug('Conexão fechada')
    connected.remove(websocket)


start_server = websockets.serve(preto_e_branco, "0.0.0.0", 8001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
