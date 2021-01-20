import pyqrcode
import png
from pyqrcode import QRCode
QRstring= input()
url = pyqrcode.create(QRstring)
url.png('qr.png', scale=8 )