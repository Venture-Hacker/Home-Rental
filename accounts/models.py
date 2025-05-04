from django.db import models
from django.contrib.auth.models import User

Create your models here.
CUSTOMER_TYPE = (
        ('ownner', 'Owner'),
        ('tenant', 'Tenant')
    )


class Customer(models.Model):
   customer_type = models.CharField(max_length=100, choices=CUSTOMER_TYPE, null=True)
