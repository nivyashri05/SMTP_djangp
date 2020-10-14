from __future__ import unicode_literals
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from mainapp.models import emailtb
from django.conf import settings
# Create your views here.test'

class Test(View):
    def get(self, request,*args, **kwargs):

        print("Anything")
        return render(request, "index.html")

    def post(self, request, *args,**kwargs):
        try:
            import os
            print("running")
            so=emailtb()
            so.Firstname = request.POST.get('First_Name')
            so.Lastname=request.POST.get('Last_Name')
            so.Emailid=request.POST.get('Email_Id')
            so.Mobilenumber=request.POST.get('Mobile_Number')
            so.Addrs=request.POST.get('Address')
            so.Place=request.POST.get('City')
            so.save()
            print("data saved sucessfully")

            email=EmailMessage("Python Notes", "Good Morning"+so.Firstname, to=[so.Emailid,"nivyarockz94@gmail.com"])
            email.send()
        except:
            import sys
            print(sys.exc_info())

        return HttpResponse("<h1> sucessfully data inserted </h1>")


test=Test.as_view()