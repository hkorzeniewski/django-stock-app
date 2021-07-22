from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from rest_framework import routers, urlpatterns, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'api/companies', views.CompanyViewSet)

urlpatterns = [
    path('table/', views.table, name='table'),
    path('form/', views.CompanyView.as_view(), name='form')

]

urlpatterns += router.urls
