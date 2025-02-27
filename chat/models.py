from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    """
    A Room can have many users and A user can be in many rooms.
    """
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(User, blank=True)

    def get_online_count(self):
        return self.online.count()
    
    def join(self, user):
        self.online.add(user)
        self.save()

    def remove(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} {self.get_online_count()}'


class Message(models.Model):
    """
    A user can post many messages and a message is only posted by one user.
    A room can have many messages and a message is only in one room.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]' 
