from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
