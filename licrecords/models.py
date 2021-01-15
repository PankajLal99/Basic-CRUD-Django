from django.db import models

# Create your models here.
class Cutomer(models.Model):
    name = models.CharField(max_length=100)
    phone=models.IntegerField(max_length=11)
    contact_person=models.CharField(max_length=100,blank=True,null=True)
    dummy=models.CharField(max_length=200,blank=True,null=True)
    dummy2=models.CharField(max_length=200,blank=True,null=True)