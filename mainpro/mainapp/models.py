from django.db import models
class emailtb(models.Model):
    Firstname=models.TextField(max_length=30, blank=True, null=True)
    Lastname=models.TextField(max_length=30, blank=True, null=True)
    Emailid=models.EmailField(max_length=30, blank=True, null=True)
    Mobilenumber=models.IntegerField( blank=True, null=True)
    Addrs=models.TextField(max_length=30, blank=True, null=True)
    Place=models.TextField(max_length=30, blank=True, null=True)
