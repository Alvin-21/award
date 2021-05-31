from django.test import TestCase
from .models import Project, Profile, Ratings, Comment
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTest(TestCase):
    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
        Ratings.objects.all().delete()
        Comment.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.tribune = Project(user=self.user, title='Moringa Tribune', description='This is a test example', link='https://alvo-tribune.herokuapp.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.tribune, Project))

    def test_save_method(self):
        self.tribune.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_delete_method(self):
        self.tribune.save_project()
        self.tribune.delete_project()
        project = Project.objects.all()
        self.assertTrue(len(project) == 0)

    def test_get_project_by_id(self):
        self.tribune.save_project()
        project = Project.get_project_by_id(self.tribune.id)
        self.assertTrue(project, self.tribune)


class ProfileTest(TestCase):
    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
        Ratings.objects.all().delete()
        Comment.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.prof = Profile(user=self.user, bio='This is a test example of my bio', email='john@test.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.prof, Profile))

    def test_save_method(self):
        self.prof.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        self.prof.save_profile()
        self.prof.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)


class RatingsTest(TestCase):
    def tearDown(self):
        Project.objects.all().delete()
        Profile.objects.all().delete()
        Ratings.objects.all().delete()
        Comment.objects.all().delete()

    def setUp(self):
        self.user = User.objects.create_user('john', email=None, password='secretpassword')
        self.tribune = Project(user=self.user, title='Moringa Tribune', description='This is a test example', link='https://alvo-tribune.herokuapp.com/')
        self.tribune.save_project()
        self.rate = Ratings(critic=self.user, project=self.tribune, design=5, usability=9, content=7)

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Ratings))

    def test_save_method(self):
        self.rate.save_rating()
        rating = Ratings.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_average_design(self):
        self.rate.save_rating()
        avg = Ratings.average_design()
        self.assertEqual(avg, 5.0)
