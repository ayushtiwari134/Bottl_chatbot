import qrcode
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20,border=1)
qr.add_data("Date: 06-01-2024 \n No of Passengers: 1 \n From: Corporation \n To: Nimhans \n Fare: Rs 20 \n Valid till: 07-01-2024 12:00 PM \n Transaction ID:1234567876")
qr.make(fit=True)
img = qr.make_image(fill_color= "black" , back_color= "white" )
img.save("tick.png")