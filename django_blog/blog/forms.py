# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment

from taggit.forms import TagWidget

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email', '')
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']


class PostForm(forms.ModelForm):
    # Input for tags, comma-separated
    tags = forms.CharField(
        required=False,
        help_text="Comma-separated tags. Example: django, python, web",
        widget=forms.TextInput(attrs={'placeholder': 'tag1, tag2, tag3', 'class': 'form-control'})

    )
    widgets = {
            'tags': TagWidget()
        }
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        # If instance is provided, populate the tags field with comma-separated names
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        if instance:
            tag_names = ', '.join([t.name for t in instance.tags.all()])
            self.fields['tags'].initial = tag_names


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        max_length=4000,
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
