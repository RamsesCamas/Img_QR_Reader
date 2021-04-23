from PIL import Image
from pyzbar import pyzbar

img = Image.open('imgs/qr.jpg')
output = pyzbar.decode(img)
data = output[0].data
data = data.decode('utf-8')
print(data)
