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