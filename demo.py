import qrcode

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)

qr.add_data("Date : 06/01/2024 \nNo of passengers : 1 \nFrom : Corporation \nTo : Nimhans \nFare : 20Rs \nValid till : 07/01/2024 12PM \nTransaction id : 63574757834\n")  

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")
