"""PJ83_db_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, re_path
from db_api import views


urlpatterns = [ 
    path('c/', views.C_data, name="C_data"),
    path('r/', views.R_data, name="R_data"),
    path('r/test/', views.R_data_filter, name="R_data_filter"),
    # re_path('^r/(?P<status>.+)/$', views.DomaintestlogList.as_view()),
    url(r'^u/(\d+)/$', views.U_data, name="U_data"),
    # url(r'^u/test/(?P<id>[^/])$', views.DomainTestLogUpdateView.as_view(), name="views.DomainTestLogUpdateView.as_view()"),
    # url(r'^d/(\d+)/$', views.D_data, name="D_data"),
    path('d/<str:tablename>/<int:id_>/', views.D_data, name="D_data"),
    path('d/<str:tablename>/all/', views.D_all_data, name="D_all_data"),
    
]

