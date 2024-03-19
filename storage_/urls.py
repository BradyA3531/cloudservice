from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login_, name='login'),
    path('storage', views.index, name='storage'),
    path('logout', views.logout_, name="logout"),
    path('storage/upload', views.upload, name= "upload"),
    path(r'^delete/(?p<id>\d+)/$', views.delete, name = "delete"),
    path(r'^more_info/(?p<id>\d+)/$', views.more_info, name = "more_info")
]