from django import forms
from .models import Musician,Album
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MusicianForm(forms.ModelForm):
	class Meta:
		model=Musician
		fields='__all__'

class AlbumForm(forms.ModelForm):
	class Meta:
		model=Album
		fields='__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']