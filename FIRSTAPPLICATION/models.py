from django.db import models

# Create your models here.

class Name(models.Model):
    Idnumber = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    contactaddress = models.CharField(null=True, max_length=30)



