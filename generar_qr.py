import qrcode
import qrcode.image.svg

args = {
    'version': 1,
    'error_correction': qrcode.constants.ERROR_CORRECT_H,
    'image_factory': qrcode.image.svg.SvgPathImage
}

with open('salida.csv') as file:
    for line in file.readlines()[1:]:
        t, v = line.strip().split('; ')
        qr = qrcode.QRCode(**args)
        qr.add_data(v)
        img = qr.make_image()
        img.save(f'QR/{t}/{v}.svg')

