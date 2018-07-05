from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'SN'
urlpatterns = [

    # SN/
    re_path(r'^$', views.home, name='default'),

    # SN/profile/  --> current logged in user's profile
    re_path(r'^profile/$', views.MyProfileView, name='myprofile'),

    # SN/profile/4  --> viewing another user's profile
    re_path(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView, name='profile'),

    # SN/profile/4/report_user/
    re_path(r'^profile/(?P<pk>[0-9]+)/report_user/$', views.ReportUserView.as_view(), name='report_user'),

    # SN/profile/4/report_user/
    re_path(r'^posts/(?P<pk>[0-9]+)/report_post/$', views.ReportPostView.as_view(), name='report_post'),

    # SN/friends/ --> Social page
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

    # SN/posts/1/delete_post
    url(r'^posts/(?P<pk>[0-9]+)/delete_post$', views.PostDelete.as_view(), name='delete_post'),

    url(r'^posts/(?P<pk>[0-9]+)/edit_post/$', views.PostUpdate.as_view(), name='edit_post'),

    # SN/posts/2/3/delete_comment
    url(r'^posts/(?P<pk>[0-9]+)/delete_comment/$', views.CommentDelete.as_view(), name='delete_comment'),

    # SN/profile/1/edit_profile
    re_path(r'^profile/(?P<pk>[0-9]+)/edit_profile/$', views.UserUpdate.as_view(), name='edit_profile'),

    # SN/profile/5/delete_profile
    re_path(r'^profile/(?P<pk>[0-9]+)/delete_profile/$', views.UserDelete.as_view(), name='delete_profile'),

    # SN/posts/7/addcomment
    url(r'^posts/(?P<pk>[0-9]+)/addcomment/$', views.add_comment_to_post, name='addcomment'),

    # SN/posts/1/Like(Unlike)
    url(r'^posts/(?P<pk>[0-9]+)/(?P<operation>.+)/$', views.change_like_post, name='change_like'),

    # SN/graph/
    url(r'^graph/$', views.graph, name='graph'),

    # SN/search_results/
    re_path(r'^search_results/$', views.search, name='search_results'),

    # SN/analysis/
    re_path(r'^analysis/$', views.analysis, name='analysis'),
    
    
    # SN/creategroup
    re_path(r'^creategroup/$', views.CreateGroupView.as_view(), name='create_group'),

    # SN/groups/
    re_path(r'^groups/$', views.groupslist, name='groups'),
    # SN/change_member
    url(r'^group_change_members/(?P<operation>.+)/(?P<pk>[0-9]+)/$', views.change_group_member, name='change_members'),

    # SN/group/pk
    re_path(r'^group/(?P<pk>[0-9]+)/$', views.group_details, name='group_details'),
    # SN/group/pk/members
    re_path(r'^group/(?P<pk>[0-9]+)/members$', views.group_members, name='group_members'),
    # SN/group/pk/addpost
    re_path(r'^group/(?P<pk>[0-9]+)/addpost$', views.Addpostgroup.as_view(), name='addpost_group'),

    # SN/group/pk/delete
    re_path(r'^group/(?P<pk>[0-9]+)/delete$', views.delete_group, name='delete_group'),
# SN/group/pk/delete_member
    re_path(r'^group/(?P<group_pk>[0-9]+)/delete_member/(?P<member_pk>[0-9]+)$', views.delete_member, name='delete_member'),


]
