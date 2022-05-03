from django.urls import path
from coreApi import game_views


urlpatterns = [
    path('games/',game_views.games),
    path('games/<int:gameId>/', game_views.game),
]