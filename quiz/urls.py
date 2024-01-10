from django.urls import path
from .views import create_battlefield, play_quiz


urlpatterns = [
    path('create_battlefield/<int:user_id>/', create_battlefield, name='create_battlefield'),
    path('play_quiz/', play_quiz, name='play_quiz'),
]
