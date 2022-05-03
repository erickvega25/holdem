from rest_framework import serializers
from coreholdem.models import Card, Player,Board,Game


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id','number','suit']

class PlayerSerializer(serializers.ModelSerializer):
    hand = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Player
        fields = ['id','name','hand','money','bet','haApostado','pasar']
        
class BoardSerializer(serializers.ModelSerializer):
    cardOfBoard = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['name','cardOfBoard']

class GameSerializer(serializers.ModelSerializer):
    player_set = PlayerSerializer(many=True,read_only=True)
    board = BoardSerializer(read_only=True)
    ganador = PlayerSerializer(read_only=False)
    class Meta:
        model = Game
        fields = ['id','pot','show','player_set','board','ganador']

