import asyncio
import websockets
import base64
from PIL import Image
import io

async def enviar_imagem(imagem_path):
    url_servidor = 'wss://a24ea60f-9742-49b2-b5f2-2e7c3e3ace54-00-2dgl6x615ioyh.picard.replit.dev'
    
    async with websockets.connect(url_servidor) as websocket:
        try:
            with open(imagem_path, "rb") as imagem_original:
                imagem64 = base64.b64encode(imagem_original.read()).decode()
                await websocket.send(imagem64)

                resultado = await websocket.recv()
                imagem_resultado = base64.b64decode(str(resultado))
                imagemB = Image.open(io.BytesIO(imagem_resultado))
                imagemB.save("NovaImagem.jpg")
        except Exception as e:
            print(f"Erro: {e}")
            
asyncio.run(enviar_imagem('./galaxy.jpg'))
