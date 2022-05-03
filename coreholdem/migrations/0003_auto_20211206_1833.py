# Generated by Django 3.2.9 on 2021-12-06 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreholdem', '0002_remove_player_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreholdem.game')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coreholdem.board'),
        ),
    ]
