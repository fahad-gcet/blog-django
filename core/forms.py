from django import forms
from .models import Post, User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body']

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
