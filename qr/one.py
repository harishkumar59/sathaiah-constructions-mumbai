import qrcode

url = "https://sathaiah-constructions-mumbai.vercel.app/"  # replace with your URL

img = qrcode.make(url)
img.save("my_qr.png")
print("QR code saved as my_qr.png")