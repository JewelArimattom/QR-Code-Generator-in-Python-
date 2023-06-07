import qrcode
import qrcode as qr
from PIL import Image
url=input("Enter the link \n")
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4,
                 )

qr.add_data(url)
qr.make(fit=True)
img= qr.make_image(fill_color="red", back_color="black")
img.save("qrcode.png")
