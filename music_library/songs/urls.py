from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongList.as_view()),
    path('songs/detail/<int:id>', views.SongDetail.as_view()),
    path('songs/like/<int:id>', views.SongLikes.as_view())
]