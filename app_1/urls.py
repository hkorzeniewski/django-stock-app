from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path
from rest_framework import routers, urlpatterns, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)

urlpatterns = [

    # path('login', views.LoginView.as_view()),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('', views.home_view, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]

urlpatterns += router.urls
