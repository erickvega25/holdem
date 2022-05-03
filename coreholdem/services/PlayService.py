from typing import Union
from coreholdem.models import Card, Game, Player, Board
class PlayService:

    NO_PLAY = 0
    PAREJA = 1
    DOBLE_PAREJA = 2
    TRIO = 3
    ESCALERA = 4
    COLOR = 5
    FULL = 6
    ESCALERA_DE_COLOR = 7
    POKER = 8
    ESCALERA_REAL = 9

    ESCALERA_REAL_NUMBERS =[1,10,11,12,13]

    def agruparCartas(player: Player,board:Board) -> list:
        cartasAgrupadas = []
        for carta in player.hand_set.all():
            cartasAgrupadas.append(carta)
        for carta in board.cardOfBoard_set.all():
            # if carta.mostradaEnMesa:
            cartasAgrupadas.append(carta)
        return cartasAgrupadas
    
    # def agruparCartasEscalera(player: Player,board:Board) -> list:
    #     cartasOrdenadasPlayer = player.hand_set.all().order_by('number')
    #     cartasOrdenadasBoard = board.cardOfBoard_set.all().order_by('number')
    #     cartasAgrupadas = []
    #     for carta in cartasOrdenadasPlayer:
    #         cartasAgrupadas.append(carta)
    #     for carta in board.cardOfBoard_set.all():
    #         # if carta.mostradaEnMesa:
    #         cartasAgrupadas.append(carta)
    #     return cartasAgrupadas

    def hasPareja(player: Player, board:Board) -> Union[int,int]:
        hasPareja = False
        numeroMasAlto = 0
        cartasAgrupadas = PlayService.agruparCartas(player,board)
        for carta in cartasAgrupadas:
            for carta2 in cartasAgrupadas:
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number:
                    hasPareja = True
                    if numeroMasAlto < carta.number:
                        numeroMasAlto = carta.number
        if hasPareja:
            return PlayService.PAREJA, numeroMasAlto
        return PlayService.NO_PLAY,None

    def hasDoblePareja(player:Player, board:Board):
        numeroMasAlto = 0
        numeroDeParejas = 0
        parejasEncontradas = []
        cartasAgrupadas = PlayService.agruparCartas(player,board)
        for carta in cartasAgrupadas:
            for carta2 in cartasAgrupadas:
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number and carta.number not in parejasEncontradas:
                    numeroDeParejas = numeroDeParejas +1
                    parejasEncontradas.append(carta.number)
                    if numeroMasAlto < carta.number:
                        numeroMasAlto = carta.number
                if numeroDeParejas == 2:
                    return PlayService.DOBLE_PAREJA, numeroMasAlto
            
        return PlayService.NO_PLAY,None

    def hasTrio(player:Player, board:Board) -> Union[int,int]:
        cartasAgrupadas = PlayService.agruparCartas(player,board)
        for carta in cartasAgrupadas:
            repeticiones = 0
            for carta2 in cartasAgrupadas:
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number:
                    repeticiones += 1
                if repeticiones == 2:
                    return PlayService.TRIO, carta.number
        return PlayService.NO_PLAY, None

    def hasEscalera(player:Player, board:Board):
        cartasOrdenadasPlayer = player.hand_set.all().order_by('number')
        cartasOrdenadasBoard = board.cardOfBoard_set.all().order_by('number')
        numeroDeCarta = None
        for card in cartasOrdenadasPlayer:
            if not numeroDeCarta:
                numeroDeCarta = card.number
                continue
            if card.number != numeroDeCarta +1:
                return PlayService.NO_PLAY, None
            numeroDeCarta = card.number
        return PlayService.ESCALERA, numeroDeCarta

    def hasColor(player:Player, board:Board):
        cartasAgrupadas = PlayService.agruparCartas(player,board)
        paloCarta = None
        numeroMasAlto = 0
        for card in cartasAgrupadas:
            if not paloCarta:
                paloCarta = card.suit
            if paloCarta != card.suit:
                return PlayService.NO_PLAY, None
            if card.number > numeroMasAlto:
                numeroMasAlto = card.number
        return PlayService.COLOR, numeroMasAlto


    def hasFull(player:Player, board:Board) ->Union[int,int]:
        hasPareja, parejaNumber = PlayService.hasPareja(player)
        hasTrio, trioNumber = PlayService.hasTrio(player)
        if hasPareja == PlayService.PAREJA and hasTrio == PlayService.TRIO and parejaNumber != trioNumber:
            return PlayService.FULL, trioNumber
        return PlayService.NO_PLAY, None


    def hasEscaleraDeColor(player:Player, board:Board):
        hasEscalera, escaleraNumber = PlayService.hasEscalera(player)
        hasColor, numeroMasAlto = PlayService.hasColor(player)
        if hasEscalera == PlayService.NO_PLAY or hasColor == PlayService.NO_PLAY:
            return PlayService.NO_PLAY, None
        return PlayService.ESCALERA_DE_COLOR, escaleraNumber

    def hasPoker(player:Player, board:Board):
        cartasAgrupadas = PlayService.agruparCartas(player,board)
        for carta in cartasAgrupadas:
            repeticiones = 0
            for carta2 in cartasAgrupadas:
                if carta.id == carta2.id:
                    continue
                if carta.number == carta2.number:
                    repeticiones += 1
                if repeticiones == 3:
                    return PlayService.POKER, carta.number
        return PlayService.NO_PLAY, None

    def hasEscaleraReal(player:Player,board:Board):
        cartasAgrupadas = PlayService.agruparCartas(player,board)
        hasColor, numeroMasAlto = PlayService.hasColor(player)
        if hasColor == PlayService.NO_PLAY:
            return PlayService.NO_PLAY, None
        for card in cartasAgrupadas:
            if not card.number in PlayService.ESCALERA_REAL_NUMBERS:
                return PlayService.NO_PLAY, None
        return PlayService.ESCALERA_REAL, numeroMasAlto


    # def calculateHigherPlay(player:Player) -> None:
    #     player.jugada = PlayService.NO_PLAY
    #     player.numMasAlto = 0
    #     jugada, numeroMasAlto = PlayService.hasPareja(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasDoblePareja(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasTrio(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasEscalera(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasColor(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasFull(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasEscaleraDeColor(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasPoker(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     jugada, numeroMasAlto = PlayService.hasEscaleraReal(player)
    #     if jugada > player.jugada:
    #         player.jugada = jugada
    #         player.numMasAlto = numeroMasAlto
    #     player.save()

    # def calculateWinner (game:Game):
    #     players = game.player_set.all()
    #     winner = None
    #     jugadaMasAlta = PlayService.NO_PLAY
    #     numeroMasAlto = 0
    #     for player in players:
    #         PlayService.calculateHigherPlay(player)
    #         if player.jugada > jugadaMasAlta:
    #             jugadaMasAlta = player.jugada
    #             numeroMasAlto = player.numMasAlto
    #             winner = player
    #         if player.jugada == jugadaMasAlta:
    #             if player.numMasAlto > numeroMasAlto:
    #                 jugadaMasAlta = player.jugada
    #                 numeroMasAlto = player.numMasAlto
    #                 winner = player
    #     game.winner = winner
    #     game.save()

