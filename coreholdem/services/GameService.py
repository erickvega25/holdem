from xmlrpc.client import Boolean
from coreholdem.models import Game, Player

class GameService:

    @staticmethod
    def pasar(player:Player) ->None:
        player.pasar = True
        player.save()
    
    @staticmethod
    def apostar(apusta:int, player:Player)->None:
        player.bet = apusta
        player.money = player.money - player.bet
        game = player.game
        game.pot = game.pot + player.bet
        game.save()
        player.haApostado = True
        player.save()
        if GameService.roundIsFinished(player.game):
            if not GameService.gameIsFinished(player.game):
                GameService.gameNextRound(player.game)
            else:
                game.ganador = player
                game.save()
        
        
    @staticmethod
    def roundIsFinished(game:Game)->Boolean:
        playersDone = 0
        for player in game.player_set.all():
            if player.pasar:
                playersDone = playersDone +1
            if player.haApostado:
                playersDone = playersDone +1
        return playersDone == game.player_set.count()

            
    @staticmethod
    def gameNextRound(game: Game)->None:
        for player in game.player_set.all():
            player.haApostado = False
            player.save()
        game.show = game.show + 1
        game.save()

    @staticmethod
    def gameIsFinished(game:Game) ->Boolean:
        hanPasado = game.player_set.filter(pasar=True).count()
        if hanPasado == game.player_set.count() -1:
            return True
        if game.show == 5:
            return True
        return False

