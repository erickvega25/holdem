from django.urls import path,include

urlpatterns = [
    path('',include('coreApi.player_urls')),
    path('',include('coreApi.game_urls')),
]