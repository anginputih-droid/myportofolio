from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.utils.html import escape

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="PBP Teaching Assistant",
            description="Help students understand web development.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "PBP Teaching Assistant")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "Ongoing")


class ProjectTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Ranu's Project",
            description="Ranu made a project.",
            category="academic",
        )

    def test_project_model(self):
        self.assertEqual(str(self.project), "Ranu's Project")
        self.assertEqual(self.project.category, "academic")
        self.assertTrue(self.project.is_ongoing)

    def test_project_page(self):
            response = self.client.get(reverse("main:show_project"))
    
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "project.html")
            self.assertContains(response, escape("Ranu's Project"))
            self.assertContains(response, "Ranu made a project")
            self.assertContains(response, "Academic Project")
            self.assertContains(response, "Ongoing")
            self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_project_page(self):
            Project.objects.all().delete()
            response = self.client.get(reverse("main:show_project"))
    
            self.assertContains(response, "No project has been added yet.")

    def test_completed_project(self):
            self.project.ended_at = timezone.now()
            self.project.save()
            response = self.client.get(reverse("main:show_project"))
    
            self.assertFalse(self.project.is_ongoing)
            self.assertContains(response, "Completed")
            self.assertNotContains(response, "Ongoing")