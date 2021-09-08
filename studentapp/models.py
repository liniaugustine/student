from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    status=models.CharField(max_length=20, default="active")
class Studentreg(models.Model):
    name=models.CharField(max_length=30)    
    contact=models.BigIntegerField()
    email=models.CharField(max_length=30)
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE) 
    status=models.CharField(max_length=20, default="active")
class Alogin(models.Model):
    ausername=models.CharField(max_length=30)
    apassword=models.CharField(max_length=8)    
    

    