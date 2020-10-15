from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Movie
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer,MovieSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
