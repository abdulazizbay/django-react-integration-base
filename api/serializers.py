from rest_framework  import serializers
from .models import *

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_id', 'code','canVote')