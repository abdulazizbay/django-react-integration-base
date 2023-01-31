from django.shortcuts import render
from .serializers import roomSerializer
from .models import Room
from rest_framework import generics

# Create your views here.
class RoomViewSet(generics.CreateAPIView):

    queryset = Room.objects.all()
    serializer_class = roomSerializer