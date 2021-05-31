from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True)
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=100)