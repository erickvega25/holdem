from coreholdem.models import  Board, Deck, Card, Game, Player
from random import randrange

class DeckService:

    CARDS_TO_PLAYER = 2
    CARDS_TO_BOARD = 5

    @staticmethod
    def createCards(deck: Deck) -> None:
        positionInDeck = 1
        for palo in range (Card.DIAMANTE,Card.CORAZON+1):
            for numero in range (1,14):
                carta = Card(number=numero,suit=Card.SUIT_NAMES[palo],deck=deck,positionInDeck=positionInDeck)
                carta.save()
                positionInDeck = positionInDeck +1

    @staticmethod
    def shuffleDeck(deck: Deck) -> None:
        posicionesGeneradas = []
        for card in deck.card_set.all():
            numeroRandom = randrange(1,53)
            while numeroRandom in posicionesGeneradas:
                numeroRandom = randrange(1, 53)     
            card.positionInDeck = numeroRandom
            posicionesGeneradas.append(numeroRandom)
            card.save()
    
    @staticmethod
    def distributeCardsToPlayer(game: Game) -> None:
        position = 0
        while position in range(DeckService.CARDS_TO_PLAYER):
            for player in game.player_set.all():
                DeckService.giveCardsToPlayer(game.deck,player,1)
            position = position +1
    

    @staticmethod
    def distributeCardsToBoard(game: Game) -> None:    
        position = 0
        while position in range(DeckService.CARDS_TO_BOARD):
            DeckService.giveCardsToBoard(game.deck,game.board,1)
            position = position +1
        
    @staticmethod
    def giveCardsToPlayer(deck:Deck, player:Player, numberOfCards) -> None:
        cards = deck.card_set.all().order_by("positionInDeck")
        cartasEntregadas = 0
        for card in cards:
            card.deck = None
            card.positionInDeck = None
            card.player = player
            card.save()
            cartasEntregadas += 1
            if cartasEntregadas == numberOfCards:
                break

    @staticmethod
    def giveCardsToBoard(deck:Deck, board:Board, numberOfCards) -> None:
        cards = deck.card_set.all().order_by("positionInDeck")
        cartasEntregadas = 0
        for card in cards:
            card.deck = None
            card.positionInDeck = None
            card.board = board
            card.save()
            cartasEntregadas += 1
            if cartasEntregadas == numberOfCards:
                break