from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):
    profile_image = forms.ImageField()

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "profile_image")

    def save(self, commit=True):
        instance = super().save(commit)
        Profile.objects.create(user=instance, image=self.cleaned_data['profile_image'])

        return instance
