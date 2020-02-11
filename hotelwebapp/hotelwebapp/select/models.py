from django.db import models
from django.contrib.auth.models import User

'''
Models in django are the crucial source of information about data. Models contain the essential fields 
and behaviors of the data being stored. Each model maps to a single database. 
''' 
#AppUser entity is a one-to-one relation with model
class AppUser(models.Model):
    user = models.OneToOneField(User, default = None, null = True, on_delete = models.CASCADE)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    appuser_name = models.CharField(max_length = 200, null = True)
    room = models.OneToOneField('Room', blank = True, on_delete = models.CASCADE, null = True)
    room_alloted = models.BooleanField(default = false)

    def __str__(self):
        return self.appuser_name

#Room class should be completed below
class Room(models.Model):
    pass
