from xmlrpc.server import SimpleXMLRPCServer
from PIL import Image, ImageOps
import io
import base64


def preto_branco(imagem):
  imagem_ori = Image.open(io.BytesIO(base64.b64decode(imagem)))
  processada = ImageOps.grayscale(imagem_ori)
  buffer = io.BytesIO()
  processada.save(buffer, format='JPEG')
  return base64.b64encode(buffer.getvalue()).decode()


server = SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(preto_branco, "preto_branco")

print("Servidor ligado")
server.serve_forever()
