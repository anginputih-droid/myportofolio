from django import forms
from main.models import Project
from django.forms import TextInput, Textarea, URLInput

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "thumbnail",
        ]

        labels = {
            "title": "Project Name",
            "description": "Project Description",
            "tech_stack": "Technology That Is Used",
            "project_url": "URL Project",
            "thumbnail": "URL Project Picture",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Python, HTML, CSS, Java, Django",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/anginputih-droid",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }