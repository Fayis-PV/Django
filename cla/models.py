from datetime import datetime
from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_number = models.BigIntegerField()
    contact_message = models.CharField(max_length=1000)
    message_time = models.TimeField(default=datetime.now)


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='imgs')
