from django.urls import path
from django.urls.resolvers import URLPattern
from coreholdem import board_views

app_name = "board"

urlpatterns = [
    path('', board_views.board, name='board')
]