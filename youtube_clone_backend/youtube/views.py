from django.shortcuts import render
from .models import CommentsAndLikes
from .serializers import InfoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class GetComment(APIView):

    def get(self, request, video_id):
        allCommentsAndLikes = CommentsAndLikes.objects.filter(video_id=video_id)
        serializer = InfoSerializer(allCommentsAndLikes, many=True)
        return Response(serializer.data)

class CommentList(APIView):

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddLike(APIView):

    def patch(self, request, video_id):
        like = CommentsAndLikes.objects.get(video_id=video_id)
        like.likes += 1
        like.save()
        return Response(status=status.HTTP_200_OK)


class VideoDetail(APIView):

    def get_object(self,pk):
        try:
            return CommentsAndLikes.objects.get(pk=pk)
        except CommentsAndLikes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        details = self.get_object(pk)
        serializer = InfoSerializer(details)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
            details=self.get_object(pk)
            serializer=InfoSerializer(details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        details = self.get_object(pk)
        details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
