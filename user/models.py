from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    client = models.ForeignKey(User,on_delete = models.CASCADE,null = False,default = None)
    hall_or_hostel = models.CharField(max_length = 200)
    room_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length = 10)
    
    def __str__(self):
        return f"{self.client.username}'s Location"