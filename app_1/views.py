from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .serializers import UserSerializer

from .forms import LoginForm

import datetime

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        
        if user is None:
            return Response({'message': 'no such user'})

        if not user.check_password(password):
            return Response({'message': 'wrong password'})

        return Response({'message':'logged in'})
    
def home_view(request):
    return render(request, 'home.html', {})

# def login_view(request):
#     username = request.data['username']
#     password = request.data['password']
#     print(username, password)
#     return render(request, 'login.html', {})


def login_view(request):
    print(request)
    form = LoginForm(request.POST or None)
    print(form)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/")

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']

#         user = User.objects.filter(username=username).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect password!')

#         # payload = {
#         #     'id': user.id,
#         #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#         #     'iat': datetime.datetime.utcnow()
#         # }

#         # token = jwt.encode(payload, 'secret',
#         #                    algorithm='HS256').decode('utf-8')

#         # response = Response()

#         # response.set_cookie(key='jwt', value=token, httponly=True)
#         # response.data = {
#         #     'jwt': token
#         # }
#         return Response({'message':'success'})
