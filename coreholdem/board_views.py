import json
from django.http import HttpResponse, JsonResponse
from coreholdem.models import Board, Game, Deck, Player
from coreholdem.services.DeckService import DeckService
from coreholdem.services.PlayerService import PlayerService


def board(request):
    board = Board()
    board.save()
    game = Game(name='Juego',board=board)
    game.save()
    deck = Deck(game=game)
    deck.save()
    DeckService.createCards(deck)
    DeckService.shuffleDeck(deck)
    PlayerService.createPlayers(game)
    DeckService.distributeCardsToPlayer(game)
    DeckService.distributeCardsToBoard(game)
    return HttpResponse("Hola bienvenido a Holdem")
