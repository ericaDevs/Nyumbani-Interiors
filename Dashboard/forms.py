from django import forms
from . import models

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ["user_name", "email", "password"]