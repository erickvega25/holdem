# Generated by Django 3.2.9 on 2022-02-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreholdem', '0006_auto_20220201_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='pot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='bet',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='money',
            field=models.IntegerField(default=1000),
        ),
    ]
