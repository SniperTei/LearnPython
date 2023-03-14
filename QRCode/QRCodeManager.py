import qrcode
import os


class QRCodeManager:
    def __init__(self, data):
        self.data = data

    def generate_qr_code(self, fill_color="black", back_color="white", imgname="qrcode.png"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(imgname)
    
    def generate_qr_code_with_logo(self, logo_path, fill_color="black", back_color="white", imgname="qrcode.png"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(imgname)

    def open_qr_code(self):
        print("Opening QR Code...")

    def delete_qr_code(self):
        os.remove("qrcode.png")
        
    def __repr__(self):
        return "QRCodeManager({})".format(self.data)
    
    def __str__(self):
        return "QRCodeManager({})".format(self.data)

qr = QRCodeManager({"name": "John", "age": 30})
