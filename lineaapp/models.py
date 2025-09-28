from django.db import models

# Create your models here.
class account(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    pswd=models.CharField(max_length=200,null=True,blank=True)

class post(models.Model):
    user=models.ForeignKey(account, on_delete=models.CASCADE) 
    lines=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True) 