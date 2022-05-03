from django.http.response import BadHeaderError
from django.urls import path
from coreApi import player_views


urlpatterns = [
    path('player/pasar/<int:playerId>/',player_views.pasar),
    path('player/apostar/<int:playerId>/',player_views.apostar),
    path('players/<int:gameId>/', player_views.players),
]