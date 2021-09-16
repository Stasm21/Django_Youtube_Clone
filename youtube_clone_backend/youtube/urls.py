from django.urls import path
from . import views


urlpatterns = [
    path('videos/postcomment/', views.CommentList.as_view()),
    path('videos/<str:video_id>/', views.GetComment.as_view()),
    path('videos/addlike/<str:video_id>/', views.AddLike.as_view())
]
