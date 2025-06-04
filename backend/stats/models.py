from django.db import models

# Create your models here.

class Action(models.Model):
    time_in_video = models.FloatField()
    action_type = models.CharField(max_length=50)
    player = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)