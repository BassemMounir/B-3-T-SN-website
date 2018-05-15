from .models import SNUser, Post, Comment
from django import forms
from django.contrib.auth.models import User

#
# class UserForm (forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#
#         fields = []


class SNUserForm (forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SNUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'location', 'profile_pic', 'birth_date',
                  'gender', 'bio']


class AddPostForm(forms.ModelForm):
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 5, 'class': "form-control"}),
    )
    class Meta:
        model = Post
        fields = ['text', 'photo']


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 5, 'class': "form-control"}),
    )

    class Meta:
        model = Comment
        fields = ['text']

