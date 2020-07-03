from django.db import models


# Create your models here.

class Description(models.Model):
    name = models.CharField(max_length=25)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    
