from django.db import models
from django.utils.timezone import datetime


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ))
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['name']
