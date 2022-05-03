from difflib import restore
from pkgutil import ImpImporter
from time import gmtime
from urllib import response
from coreholdem.models import Game
from django.http import JsonResponse
from coreholdem.serializers import GameSerializer


def games(request):
    games = Game.objects.all()
    serializer = GameSerializer(games,many=True)
    return JsonResponse(serializer.data,safe=False)

def game(request, gameId):
    try:
        game = Game.objects.get(id=gameId)
    except Game.DoesNotExist:
        return JsonResponse(status=404)
    serializer = GameSerializer(game)
    return JsonResponse(serializer.data)