from email.mime import image
import qrcode
from PIL import Image

cadena=input("introduzca el texto para el QR:")
imagen= qrcode.make(cadena)

nombre_imagen = input("introduzca el nombre de la imagen:") + ".jpg"
archivo_imagen= open(nombre_imagen,"wb")
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = "/" + nombre_imagen
Image.open(ruta_imagen).show()