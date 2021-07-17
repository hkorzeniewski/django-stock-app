from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from rest_framework import routers, urlpatterns, viewsets
from . import views


urlpatterns = [

    path('table/', views.table_view, name='table'),
    path('form/', views.CompanyView.as_view(), name='form')

]
