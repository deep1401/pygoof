import pyqrcode

def create_qr(link):
    url=pyqrcode.create(link)
    url.svg('uca-url.svg',scale=8)
    print(url.terminal(quiet_zone=1))
    print('QR code stored in local directory! ')

link=input("Enter link to create url: ")
create_qr(link)
