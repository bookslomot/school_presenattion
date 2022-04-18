from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserSerializer


class UserDetailAPIVIew(generics.RetrieveAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = (AllowAny, )





