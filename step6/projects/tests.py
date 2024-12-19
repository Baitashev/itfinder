from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Project


class ProjectsViewTest(TestCase):
    def test_projects_view(self):
        # Используем reverse для получения URL-адреса представления 'projects'
        url = reverse('projects')
        response = self.client.get(url)

        # Проверяем, что ответ содержит код состояния 200
        self.assertEqual(response.status_code, 200)

        # Проверяем, что используется ожидаемый шаблон
        self.assertTemplateUsed(response, 'projects/projects.html')
    def test_projects_view_status_code(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

class ProjectModelTest(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(title='Test Project', description='This is a test project')
        self.assertEqual(project.title, 'Test Project')
        self.assertEqual(project.description, 'This is a test project')

    def test_project_list_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/projects.html')