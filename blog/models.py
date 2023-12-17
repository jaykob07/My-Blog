from django.db import models
from django.db.models.fields import URLField
import datetime

class Post(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    url = URLField(blank=True)
