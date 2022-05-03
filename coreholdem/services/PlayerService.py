from coreholdem.models import Game, Player
class PlayerService:

    @staticmethod
    def createPlayers(game : Game) -> None:
        player1 = Player(name="Erick",game=game,)
        player2 = Player(name="Julio",game=game,)
        player3 = Player(name="Pepe",game=game,)
        player1.save()
        player2.save()
        player3.save()