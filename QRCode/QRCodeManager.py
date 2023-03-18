import qrcode
import os
import sys
from PIL import Image

class QRCodeManager:
    def __init__(self, data):
        self.data = data

    def generate_qr_code(self, fill_color="black", back_color="white", img_name="qrcode.png"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        # 保存二维码图片名 打开和删除时候要用到
        self.img_name = img_name

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(img_name)
    
    def generate_qr_code_with_logo(self, logo_path, fill_color="black", back_color="white", img_name="qrcode.png"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(img_name)

    def open_qr_code(self):
        # 用系统默认的图片查看器打开图片
        print("Opening QR Code...")
        spect= Image.open(self.img_name)
        spect.show()

    def delete_qr_code(self):
        # 删除图片
        print("Deleting QR Code...")
        os.remove(self.img_name)
        
    def __repr__(self):
        return "QRCodeManager({})".format(self.data)
    
    def __str__(self):
        return "QRCodeManager({})".format(self.data)


def main():
    print("main ")
    qr_data = sys.argv[1]
    if qr_data:
        qr = QRCodeManager(qr_data)
        qr.generate_qr_code()
        qr.open_qr_code()
        print("QR Code Generated!")
        print(f"{qr}")

if __name__ == "__main__":
    main()