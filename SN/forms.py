from .models import SNUser, Post, Comment, ReportUser
from django import forms


class SNUserForm(forms.ModelForm):
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


class ReportUserForm(forms.ModelForm):
    CHOICES = [('select1', 'This is a fake account'),
               ('select2', 'This person has inappropriate personal information (profile picture, bio section...etc.)'),
               ('select3', 'This person is sharing inappropriate/offensive posts'),
               ('select4', 'This person is annoying me'),
               ('select5', 'Other...')
               ]

    text = forms.CharField(required=False,
                           max_length=1000,
                           widget=forms.Textarea(attrs={'rows': 5, 'class': "form-control"}),
                           )

    report_option = forms.ChoiceField(choices=CHOICES, required=True, widget=forms.RadioSelect())

    class Meta:
        model = ReportUser
        fields = ['report_option', 'text']
