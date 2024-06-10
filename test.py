from xmlrpc.client import ServerProxy
import base64
import io
from PIL import Image

url_servidor = 'dddddc04-f2f9-4153-ae32-0172e5096b6f-00-gqgkds7g0wct.spock.replit.dev:8000'

servidor = ServerProxy(f'https://{url_servidor}')

imagem = "./galaxy.jpg"

with open(imagem,"rb") as imagem_original:
  imagem64 = base64.b64encode(imagem_original.read()).decode()


resultado = servidor.preto_branco(imagem64)
#resultado = servidor.inverter(imagem64)
#resultado = servidor.colorir(imagem64)

imagem_resultado = base64.b64decode(str(resultado))
imagemB = Image.open(io.BytesIO(imagem_resultado))

imagemB.save("NovaImagem.jpg")