from django.db import models

# Create your models here.


class My_mode(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    img = models.ImageField(upload_to="img/", blank=True, null=True)


class poshtibani_mdoel(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
