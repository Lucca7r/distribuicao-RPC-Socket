import asyncio
import websockets
import base64
from PIL import Image
import io
import time
from concurrent.futures import ThreadPoolExecutor

# Função para enviar uma única imagem
async def enviar_imagem(url_servidor, imagem_path, index):
    try:
        with open(imagem_path, "rb") as imagem_original:
            imagem64 = base64.b64encode(imagem_original.read()).decode()
            async with websockets.connect(url_servidor) as websocket:
                await websocket.send(imagem64)
                resultado = await websocket.recv()
                imagem_resultado = base64.b64decode(str(resultado))
                imagemB = Image.open(io.BytesIO(imagem_resultado))
                imagemB.save(f"./out/image_pb_{index}.jpg")
    except Exception as e:
        print(f"Erro ao enviar/receber a imagem {imagem_path}: {e}")

# Função modificada para enviar imagens em paralelo
async def enviar_imagens(imagens_paths):
    inicio = time.time()
    url_servidor = 'wss://a24ea60f-9742-49b2-b5f2-2e7c3e3ace54-00-2dgl6x615ioyh.picard.replit.dev:3000'
    
    # Usar ThreadPoolExecutor para enviar imagens em paralelo
    with ThreadPoolExecutor(max_workers=len(imagens_paths)) as executor:
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(
                executor, 
                lambda imagem_path=imagem_path, index=index: asyncio.run(enviar_imagem(url_servidor, imagem_path, index))
            ) for index, imagem_path in enumerate(imagens_paths)
        ]
    await asyncio.gather(*tasks)
    
    print(f"Tempo total: {time.time() - inicio}")

# Lista de caminhos das imagens a serem enviadas
imagens_paths = ['./assets/galaxy.jpg', './assets/tigre.jpg', './assets/bigbang.jpg', './assets/unsplash (1).jpg', './assets/unsplash (2).jpg', './assets/unsplash (3).jpg', './assets/unsplash (4).jpg', './assets/unsplash (5).jpg']
asyncio.run(enviar_imagens(imagens_paths))
