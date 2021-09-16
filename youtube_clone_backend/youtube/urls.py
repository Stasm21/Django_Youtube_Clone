from django.urls import path
from . import views


urlpatterns = [
    path('videos/postcomment/', views.CommentList.as_view()),
    path('videos/<str:videoId>/', views.GetComment.as_view()),
    path('videos/addlike/<str:videoId>/', views.AddLike.as_view())
]
