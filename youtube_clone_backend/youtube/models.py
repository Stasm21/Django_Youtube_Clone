from django.db import models

# Create your models here.
class CommentsAndLikes(models.Model):
    videoId = models.CharField(max_length=100)
    comments = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
