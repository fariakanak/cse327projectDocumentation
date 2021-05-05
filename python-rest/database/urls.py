"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from hrm.api import *
from hrm.admin import admin_site
from django.conf import settings
from django.conf.urls.static import static
from templates.registration import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hrmadmin/', admin_site.urls),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='User Authentication API'),
    url(r'^api/user_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/user_list/(?P<email_id>\d+)/$', UserDetail.as_view(), name='user_list'),
    url(r'^api/dept_list/$', DeptList.as_view(), name='dept_list'),
    url(r'^api/dept_list/(?P<dept_id>\d+)/$', DeptDetail.as_view(), name='dept_list'),
    url(r'^api/document_list/$', DocumentList.as_view(), name='document_list'),
    url(r'^api/document_list/(?P<record_no>\d+)/$', DocumentDetail.as_view(), name='document_list'),
    url(r'^api/team_list/$', TeamList.as_view(), name='team_list'),
    url(r'^api/team_list/(?P<team_no>\d+)/$', TeamDetail.as_view(), name='team_list'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^fileupload/$', auth_views.LoginView.as_view(template_name='registration/fileupload.html'), name='fileupload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
