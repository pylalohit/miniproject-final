from django.db import models
from django.db.models.fields import DecimalField, EmailField, IntegerField
from django.contrib.auth.models import User



# Create your models here.


class product(models.Model):
    pid = IntegerField(null=False, primary_key=True)
    pname = models.TextField()
    pprice = models.IntegerField()
    pquantity = models.IntegerField()
    pavailability = models.TextField(max_length=150)
    pdescription = models.TextField(max_length=200)
    user = models.ForeignKey(User,on_delete = models.CASCADE,)

class userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    shopname = models.TextField(max_length=150)
    phonenumber = models.TextField(max_length=16)
    passkey = models.TextField(max_length=20)
    username = models.TextField(max_length=150,default=None)
    email = models.EmailField(default=None)
    address = models.TextField(max_length=200)

    