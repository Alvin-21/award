from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Avg

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True)
    description = models.CharField(max_length=1500)
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project_by_id(cls, id):
        project = cls.objects.get(id=id)
        return project


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    bio = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()    


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

    def save_rating(self):
        self.save()

    @classmethod
    def average_design(cls):
        avg = cls.objects.aggregate(avg_design=Avg('design'))
        return avg['avg_design']

    @classmethod
    def average_usability(cls):
        avg = cls.objects.aggregate(avg_usability=Avg('usability'))
        return avg

    @classmethod
    def average_content(cls):
        avg = cls.objects.aggregate(avg_content=Avg('content'))
        return avg


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments