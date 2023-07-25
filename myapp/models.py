from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


class Videos(models.Model):
    thumbnail = models.ImageField(upload_to='media/kayondo/F0563249563210B8/codes/Vs Code/Django/youtubeClone-django/youtubeClone_django/static/thumbnails/')
    video_time = models.TimeField()
    channel_picture = models.ImageField(upload_to='media/kayondo/F0563249563210B8/codes/Vs Code/Django/youtubeClone-django/youtubeClone_django/static/channel-pictures/')
    video_title = models.CharField(max_length=500)
    video_author = models.CharField(max_length=100)
    views = models.CharField(max_length=50) 
    period = models.CharField(max_length=100) 