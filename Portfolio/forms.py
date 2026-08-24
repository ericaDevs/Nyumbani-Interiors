from . import models
from django import forms

class CreateNewProject(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'category', 'description', 'location', 'client_name', 'completion_year', 'main_image']

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description:
            return description.strip()
        return description

