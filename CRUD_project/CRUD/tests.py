from django.test import TestCase
from django.urls import reverse
from .models import Project

class ProjectTests(TestCase):

    def setUp(self):
        Project.objects.create(name='webapp development',description='webapp dev in django')

    def testProjectDetails(self):
        project = Project.objects.get(id=1)
        modelName = f'{project.name}'
        self.assertEquals(modelName, 'webapp development')