"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from my_app import views

app_name = "my_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'my_app/', include("my_app.urls", namespace='my_app')),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login_user/$', views.login_user, name="login_user"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^logout_user/$', views.logout_user, name="logout_user"),
    url(r'^create/$', views.create, name="create"),
    url(r'^update_event(?P<pk>\d+)/$', views.update_event, name="update_event"),
    url(r'^delete_event(?P<pk>\d+)/$', views.delete_event, name="delete_event"),
    url(r'^create_task(?P<pk>\d+)/$', views.create_task, name="create_task"),
    url(r'^task_details/$', views.task_details, name="task_details"),
    url(r'^all_events/$', views.all_event, name="all_events"),
    url(r'^event_detail(?P<pk>\d+)/$', views.event_details, name="event_details"),
]
