from django.shortcuts import render
import qrcode
from io import BytesIO  
from django.http import HttpResponse



def generate_qr_code(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        qr = qrcode.make(url)
        response = HttpResponse(content_type="image/png")
        qr.save(response, "PNG")
        return response
    return render(request, 'generate_qr_code.html')