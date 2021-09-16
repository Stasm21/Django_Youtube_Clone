from rest_framework import serializers
from .models import CommentsAndLikes

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsAndLikes
        fields = ['videoId', 'comments', 'likes']
