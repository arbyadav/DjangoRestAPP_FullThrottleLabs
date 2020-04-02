"""RestApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from API.views import *

urlpatterns = [
    url(r'^api/auth/$', UsersAuthentication.as_view(),
        name="user Authentication API"),

    url(r'^api/members_list/$',
        MembersList.as_view(), name="members_list"),
    url(r'^api/members_list/(?P<member_id>\d+)/$',
        MembersDetail.as_view(), name="members_detail"),

    url(r'^api/users_list/$',
        UsersList.as_view(), name="users_list"),
    url(r'^api/users_list/(?P<user_id>\d+)/$',
        UsersDetail.as_view(), name="user_detail"),

    url(r'^api/activities_list/$',
        ActivitiesList.as_view(), name="activities_list"),
    url(r'^api/activities_list/(?P<activity_id>\d+)/$',
        ActivitiesDetail.as_view(), name="activity_detail"),

]
