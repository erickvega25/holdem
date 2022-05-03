from django.core.management.base import BaseCommand, CommandError
from coreholdem.models import Game


class Command(BaseCommand):
    help = 'Cambiar bote de la mesa'

    def add_arguments(self, parser):
        parser.add_argument('nuevo_bote', type=int)

    def handle(self, *args, **options):
        nuevo_bote = options.get('nuevo_bote', None)
        try:
            game = Game.objects.get(id=47)
        except Game.DoesNotExist:
            raise CommandError('No existe el Game')

        game.pot = nuevo_bote
        game.save()

        self.stdout.write('El bote se ha cambiado correctamente')