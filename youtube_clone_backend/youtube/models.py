from django.db import models

# Create your models here.
class CommentsAndLikes(models.Model):
    video_id = models.CharField(max_length=100)
    comments = models.CharField(max_length=1000)
    replies = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
