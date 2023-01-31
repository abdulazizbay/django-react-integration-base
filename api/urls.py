
from django.urls import path
from .views import *

urlpatterns = [
    path('room', RoomViewSet.as_view()),
]