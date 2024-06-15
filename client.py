import asyncio
import websockets
import base64
from PIL import Image
import io
import time

async def enviar_imagens(imagens_paths):
    inicio = time.time()
    url_servidor = 'wss://a24ea60f-9742-49b2-b5f2-2e7c3e3ace54-00-2dgl6x615ioyh.picard.replit.dev:3000'
    
    async with websockets.connect(url_servidor) as websocket:
        for index, imagem_path in enumerate(imagens_paths):
            try:
                with open(imagem_path, "rb") as imagem_original:
                    imagem64 = base64.b64encode(imagem_original.read()).decode()
                    await websocket.send(imagem64)

                    resultado = await websocket.recv()
                    imagem_resultado = base64.b64decode(str(resultado))
                    imagemB = Image.open(io.BytesIO(imagem_resultado))
                    # Garante que cada imagem salva tenha um nome único
                    imagemB.save(f"./out/image_pb_{index}.jpg")
            except Exception as e:
                print(f"Erro ao enviar/receber a imagem {imagem_path}: {e}")
    
    print(f"Tempo total: {time.time() - inicio}")

# Lista de caminhos das imagens a serem enviadas
imagens_paths = ['./assets/galaxy.jpg', './assets/bigbang.jpg', './assets/tigre.jpg', './assets/unsplash (1).jpg', './assets/unsplash (2).jpg', './assets/unsplash (3).jpg', './assets/unsplash (4).jpg', './assets/unsplash (5).jpg']
asyncio.run(enviar_imagens(imagens_paths))