from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description =CharField(max_length=400)
    image = ImageField(upload_to="iportfolio/images/")
   