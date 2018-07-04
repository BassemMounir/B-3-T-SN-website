from django.contrib import admin

# Register your models here.
from . models import SNUser, Post, Like, Comment, Friend, ReportUser, ReportPost

admin.site.register(SNUser)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Friend)
admin.site.register(ReportUser)
admin.site.register(ReportPost)
