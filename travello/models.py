from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    picture = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

