from django.shortcuts import render,HttpResponse
from .models import Reg
# from django.contrib.auth import authenticate
from django.core.mail import send_mail  # Assuming you are sending OTP via email
from django.conf import settings
import random
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.POST.get('username')
        mail = request.POST.get('Email')
        phn = request.POST.get('Phno')
        qual = request.POST.get('qual')
        data = Reg.objects.create(name = name,username = user,email = mail,phno = phn,qualification = qual)
        data.save()
    return render(request,'index.html')


def log(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = random.randint(100000,999999)
        send_mail(
            otp,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False

        )
        print('login success')
        return HttpResponse('login successful')
    return render(request,'login.html')




