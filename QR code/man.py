import qrcode
url=input("Enter you URL").strip()
loc="C:\\Users\\DhanushKumarMahaling\\Desktop\\my work\\My Training\\qr.png"

qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(loc)
print("qrcode completed")