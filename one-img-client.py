import asyncio
import websockets
import base64
from PIL import Image
import io
import os
from concurrent.futures import ThreadPoolExecutor

# Função para enviar um pedaço da imagem
async def enviar_pedaco_imagem(url_servidor, pedaco_imagem, index):
    try:
        imagem64 = base64.b64encode(pedaco_imagem).decode()
        async with websockets.connect(url_servidor) as websocket:
            await websocket.send(imagem64)
            resultado = await websocket.recv()
            imagem_resultado = base64.b64decode(str(resultado))
            if not os.path.exists("./out"):
                os.makedirs("./out")
            with open(f"./out/pedaco_{index}.jpg", "wb") as f:
                f.write(imagem_resultado)
    except Exception as e:
        print(f"Erro ao enviar/receber o pedaço da imagem: {e}")

# Função para dividir a imagem em pedaços
def dividir_imagem(imagem_path, num_pedacos):
    imagem = Image.open(imagem_path)
    largura, altura = imagem.size
    pedaco_largura = largura // num_pedacos
    pedacos = []

    for i in range(num_pedacos):
        esquerda = i * pedaco_largura
        direita = (i + 1) * pedaco_largura if i < num_pedacos - 1 else largura
        pedaco = imagem.crop((esquerda, 0, direita, altura))
        pedacos.append(pedaco)

    return pedacos

# Função principal para processar a imagem
async def processar_imagem(imagem_path, url_servidor, num_pedacos):
    pedacos = dividir_imagem(imagem_path, num_pedacos)
    tasks = []

    for index, pedaco in enumerate(pedacos):
        with io.BytesIO() as output:
            pedaco.save(output, format="JPEG")
            pedaco_imagem = output.getvalue()
            task = enviar_pedaco_imagem(url_servidor, pedaco_imagem, index)
            tasks.append(task)

    await asyncio.gather(*tasks)
    montar_imagem("./out", "out/imagem_montada.jpg")  # Chama a função de montagem após processar todos os pedaços

# Função para montar a imagem a partir dos pedaços
def montar_imagem(diretorio_pedacos, imagem_saida):
    pedacos = []
    largura_total = 0
    altura = 0
    arquivos_pedacos = sorted([f for f in os.listdir(diretorio_pedacos) if os.path.isfile(os.path.join(diretorio_pedacos, f))])

    for arquivo in arquivos_pedacos:
        caminho_completo = os.path.join(diretorio_pedacos, arquivo)
        with Image.open(caminho_completo) as img:
            pedacos.append(img.copy())  # Copie a imagem para evitar o erro ao fechar o arquivo
            largura_total += img.width
            altura = img.height

    imagem_montada = Image.new('RGB', (largura_total, altura))
    posicao_atual = 0
    for pedaco in pedacos:
        imagem_montada.paste(pedaco, (posicao_atual, 0))
        posicao_atual += pedaco.width

    imagem_montada.save(imagem_saida)

# Exemplo de uso
if __name__ == "__main__":
    asyncio.run(processar_imagem("./assets/baloes.jpg", "wss://a24ea60f-9742-49b2-b5f2-2e7c3e3ace54-00-2dgl6x615ioyh.picard.replit.dev:3000", 4))