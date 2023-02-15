#Encode decode data to a QR code !

import qrcode

data_encode = 'NO PAIN NO GAIN'

qr = qrcode(version = 1, box_size = 20, border = 5)
qr.add_data(data_encode)
qr.make(fit=True)

img = qr.make_image(fill_color = 'blue', black_color = 'white')
img.save('D:/Nicky/Videos/qrcode.png')