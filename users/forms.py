from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from .models import Profile
from blog.models import Comment

class LoginUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class UserRegistrationForm(UserCreationForm):
    #email = forms.EmailField()
    #first_name = forms.CharField(max_length=25)
    #last_name = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'placeholder': 'Add comment...'
        })
    )
    class Meta:
        model = Comment
        fields = ['comment']