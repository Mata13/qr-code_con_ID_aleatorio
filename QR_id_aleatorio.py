# Este es un programa que genera un QR Code con un ID aleatorio de 9 dígitos

# Importamos las librerías que vamos a usar
import qrcode
from random import randint

# Guardamos el qr creado con su ID de 9 dígitos
img = qrcode.make( 'QR-ID : %d' % randint(100000000, 999999999) )

# Imprimimos la imagen
print(type(img))
print(img.size)

# Guardamos la imagen en el directorio de trabajo con su respectivo nombre
img.save('/home/zickgamer/Documentos/Developer/Projects/QR_Flask_Gen/QR/idqr.png')