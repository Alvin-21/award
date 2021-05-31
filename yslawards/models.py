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


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    bio = models.CharField(max_length=200)
    email = models.EmailField()


class Ratings(models.Model):
    RATING_VALUES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATING_VALUES, default=0)
    usability = models.IntegerField(choices=RATING_VALUES, default=0)
    content = models.IntegerField(choices=RATING_VALUES, default=0)
