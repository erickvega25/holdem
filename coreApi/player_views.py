import json
from signal import pthread_kill
from time import process_time_ns
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from coreholdem.models import Player
from coreholdem.serializers import PlayerSerializer
from coreholdem.services.GameService import GameService

def players(request,gameId):
    if request.method == "GET":
        players = Player.objects.filter(game__id=gameId)
        sereializer = PlayerSerializer(players,many=True)
        return JsonResponse(sereializer.data,safe=False)

def pasar(request, playerId):
    if request.method != "PUT":
        return HttpResponseForbidden()
    try:
        player = Player.objects.get(pk=playerId)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    GameService.pasar(player)
    return JsonResponse({"status":"OK"},status=200)


def apostar(request,playerId):
    if request.method != "PUT":
        return HttpResponseForbidden()
    try:
        player = Player.objects.get(pk=playerId)
    except Player.DoesNotExist:
        return HttpResponse(status=404)
    content = json.loads(request.body)
    contenido = content["bet"]
    apuesta = int(contenido)
    print(type(apuesta))
    GameService.apostar(apuesta, player)
    return JsonResponse({"status":"OK"},status=200)