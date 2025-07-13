import qrcode
data="sarkarsouvik2343@gmail.com"
qr=qrcode.make(data)
qr.save("souvik@gmail.png")
print("QR code generate succesfully")
