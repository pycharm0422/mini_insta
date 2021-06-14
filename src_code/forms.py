from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Post, Comments
from django.forms import ModelForm, fields


class AddPosts(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['user', 'post', 'tag']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
