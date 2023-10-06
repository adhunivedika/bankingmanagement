from django.db import models
from django.forms import ModelForm
# Create your models here.

import datetime
class District(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.name
class Branches(models.Model):
    district=models.ForeignKey(District,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
accounttype_CHOICES=[
    ("Savings account" ,"Savings account"),
    ("Current account","Current account")
    ]
class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phonenumber = models.PositiveIntegerField()
    address = models.TextField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField( max_length=50)
    accounttype=models.CharField(max_length=250,choices=accounttype_CHOICES,default=None)
    materials_provided=models.CharField(max_length=250)

    class Meta:
        ordering=['name']
    def __str__(self):
        return '{}'.format(self.name)

