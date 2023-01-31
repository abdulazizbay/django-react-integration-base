from django.db import models

# Create your models here.
class Room(models.Model):
    room_id = models.IntegerField()
    code = models.CharField(max_length=6)
    canVote = models.BooleanField(default=False)

    def __str__(self):
        return self.room_id