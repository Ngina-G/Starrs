from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post,Profile,Rating
from pyuploadcare.dj.forms import ImageField



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text="Required .Email address")
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        
class PostForm(forms.ModelForm):
    image =ImageField(label='')
    
    class Meta:
        model = Post
        fields = ('image', 'title', 'description', 'url',)
        
