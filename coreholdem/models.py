from pyexpat import model
from django.db import models



class Game(models.Model):
    name = models.CharField(max_length=255)
    board = models.OneToOneField("Board",on_delete=models.CASCADE,null=True)
    pot = models.IntegerField(null=False,default=0)
    show = models.IntegerField(null=False, default=3)
    ganador = models.ForeignKey("Player",on_delete=models.CASCADE,null=True,default=None,related_name="ganador")
    

class Deck(models.Model):
    game = models.OneToOneField(Game,on_delete=models.CASCADE)

 
class Player(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    money = models.IntegerField(null=False,default=1000)
    bet = models.IntegerField(null=False,default=0)
    haApostado = models.BooleanField(default=False)
    pasar = models.BooleanField(default=False)

class Board(models.Model):
    name = models.CharField(default="mesa",max_length=255)

class Card(models.Model):
    
    DIAMANTE = 0
    PICA = 1
    TREBOL = 2
    CORAZON = 3

    SUIT_NAMES = ["DIAMANTE","PICA","TREBOL","CORAZON"]
    
    number = models.IntegerField(null=False)
    suit = models.CharField(max_length=20,null=False)
    deck = models.ForeignKey(Deck,on_delete=models.CASCADE,null=True)
    positionInDeck = models.IntegerField(null=True)
    player = models.ForeignKey(Player,on_delete=models.CASCADE,null=True,related_name='hand')
    board = models.ForeignKey(Board,on_delete=models.CASCADE,null=True,related_name='cardOfBoard')
    mostradaEnMesa = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.number) + " de " +self.suit