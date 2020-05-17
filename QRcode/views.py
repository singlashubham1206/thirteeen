from django.shortcuts import render
from django.http import HttpResponse
import qrcode

def generateQR(request):
    if request.method == 'POST':
        text_data=request.POST['text']
        print("Data entered by user : ",text_data)
        img = qrcode.make(text_data)
        print("QR code generated....")
        img.save('static/images/user_data_qr.png')
        print("QRcode is saved")
        res = render(request,'QRcode/home.html',{'qrcode':'user_data_qr.png'})
    else:
        res = render(request,'QRcode/home.html')
    return res
