from django.db import models

# Create your models here.


class Contact(models.Model):
    Name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
