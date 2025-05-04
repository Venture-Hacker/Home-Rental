from django.db import models
from django import forms
# from widgets import BootstrapDateTimePickerInput
from bootstrap_datepicker_plus import *
# DatePickerInput

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.city,filename)

class House(models.Model):
    image = models.ImageField(upload_to=uploaded_location,null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    house_owner = models.CharField(max_length=100)
    house_number = models.IntegerField()
    cost_per_day = models.CharField(max_length=50)
    content = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return "/house/newhouse/%s/" % (self.id)

class Order(models.Model):
    city = models.CharField(max_length=100)
    tenant_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    from_date = models.DateTimeField()
    to = models.DateTimeField()

    def __str__(self):
        return self.city

    def get_absolute_url(self):
        return "/house/detail/%s/" % (self.id)

class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()


class Tenant(models.Model):
    owner_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=200)


    def __str__(self):
        return self.name  

class Owner(models.Model):
    owner_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=200)


    def __str__(self):
        return self.name