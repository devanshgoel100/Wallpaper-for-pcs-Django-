from tokenize import Name
from unicodedata import name
from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=122)
    Email=models.CharField(max_length=122)
    PhoneNo=models.CharField(max_length=12)
    City=models.CharField(max_length=122)
    Address=models.CharField(max_length=122)
    Zip=models.CharField(max_length=12)
   # ch=models.CharField(max_length=122)
    date=models.DateField()

    def __str__(self):
        return self.Name + " "+ self.PhoneNo

