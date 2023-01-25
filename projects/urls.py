from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create_job_page/', views.create_job_page, name='create_job_page'),
]