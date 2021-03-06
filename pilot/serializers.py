from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Movie
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"