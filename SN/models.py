from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class SNUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True, )
    location = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.FileField(null=True, default='../media/anonymous.jpg')  # default profile pic

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.first_name+" "+self.last_name


class Post(models.Model):
    owner = models.ForeignKey(SNUser, related_name='posts', on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    photo = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    current_user_like = models.BooleanField(default=False)
    is_group_post = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('SN:post_detail', args=[self.slug])

    def __str__(self):
        return self.owner.username + " \n\t " + self.text


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(SNUser,related_name='usercomments', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    photo = models.FileField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username + " \n\t " + self.text


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)
    owner = models.ForeignKey(SNUser, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username


class Friend(models.Model):
    friends = models.ManyToManyField(SNUser)
    current_user = models.ForeignKey(SNUser, related_name="owner", null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.friends.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.friends.remove(new_friend)


class ReportUser(models.Model):
    CHOICES = [('select1', 'This is a fake account'),
               ('select2', 'This person has inappropriate personal information (profile picture, bio section...etc.)'),
               ('select3', 'This person is sharing inappropriate/offensive posts'),
               ('select4', 'This person is annoying me'),
               ('select5', 'Other...')
               ]

    text = models.CharField(max_length=5000)
    owner = models.ForeignKey(SNUser, related_name='reporting', on_delete=models.CASCADE)
    reported_user = models.ForeignKey(SNUser, related_name='reported', on_delete=models.CASCADE)
    report_option = models.CharField(choices=CHOICES, max_length=100)


class ReportPost(models.Model):
    CHOICES = [('select1', 'This post is annoying/not interesting'),
               ('select2', "The post's content is offensive/abusive (bad language,threatening,violence,..etc."),
               ('select3', "Spam post"),
               ('select4', 'Other...'),
               ]

    text = models.CharField(max_length=5000)
    owner = models.ForeignKey(SNUser, related_name='reporting_user', on_delete=models.CASCADE)
    reported_post = models.ForeignKey(Post, related_name='reported_post', on_delete=models.CASCADE)
    reported_post_user = models.ForeignKey(SNUser, related_name='reported_post_user', on_delete=models.CASCADE)
    report_option = models.CharField(choices=CHOICES, max_length=100)
    
    
class Group(models.Model):
    members = models.ManyToManyField(SNUser)
    posts = models.ManyToManyField(Post)
    admin = models.ForeignKey(SNUser, related_name="admin", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    photo = models.FileField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
