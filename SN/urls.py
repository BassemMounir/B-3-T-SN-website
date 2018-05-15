from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'SN'
urlpatterns = [

    # SN/profile/
    re_path(r'^profile/$', views.MyProfileView, name='myprofile'),

    re_path(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView, name='profile'),

    re_path(r'^friends/$', views.FriendsView, name='friends'),

    # SN/register/

    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),

    # SN/login/
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='SN/login.html'), name='login'),

    # SN/logout/
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # SN/addpost
    re_path(r'^addpost/$', views.Addpostview.as_view(), name='addpost'),

    url(r'^connect/(?P<operation>.+)/(?P<pk>[0-9]+)/$', views.change_friends, name='change_friends'),

    # SN/home
    re_path(r'^home/$', views.home, name='home'),

    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_details, name='post_details'),

    # SN/posts/1/addcomments
    url(r'^posts/(?P<pk>[0-9]+)/delete_post$', views.PostDelete.as_view(), name='delete_post'),

    url(r'^posts/(?P<pk>[0-9]+)/edit_post$', views.PostUpdate.as_view(), name='edit_post'),

    #SN/posts/post_num/comment_num/delete_comment
    url(r'^posts/(?P<pk>[0-9]+)/delete_comment$', views.CommentDelete.as_view(), name='delete_comment'),

    re_path(r'^profile/(?P<pk>[0-9]+)/edit_profile$', views.UserUpdate.as_view(), name='edit_profile'),

    re_path(r'^profile/(?P<pk>[0-9]+)/delete_profile$', views.UserDelete.as_view(), name='delete_profile'),
    url(r'^posts/(?P<pk>[0-9]+)/addcomment$', views.add_comment_to_post, name='addcomment'),

    # SN/posts/1/Like(Unlike
    url(r'^posts/(?P<pk>[0-9]+)/(?P<operation>.+)/$', views.change_like_post, name='change_like'),

    # SN/graph
    url(r'^graph/$', views.graph, name='graph'),

    # SN/search_results
    re_path(r'^search_results/$', views.search, name='search_results'),

    # SN/analysis
    re_path(r'^analysis/$', views.analysis, name='analysis'),

    re_path(r'^$', views.home, name='default'),



]
