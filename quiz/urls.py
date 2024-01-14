from django.urls import path
from .views import create_battlefield, play_quiz, edit_battlefield


urlpatterns = [
    path('create_battlefield/<int:user_id>/', create_battlefield, name='create_battlefield'),
    path('edit_battlefield/<int:battlefield_id>/', edit_battlefield, name='edit_battlefield'),
    path('play_quiz/', play_quiz, name='play_quiz'),

]
