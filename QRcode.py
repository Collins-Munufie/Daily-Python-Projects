import pyqrcode
import png
from pyqrcode import QRCode

# Generate QR code for a given URL
s = "www.greeksforgreeks.org"

# Generate QR code
url = pyqrcode.create(s)

# Save the QR code in different formats
url.svg("myqr.svg", scale = 8)

url.png("myqr.png", scale = 6)