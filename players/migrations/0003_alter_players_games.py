# Generated by Django 3.2.7 on 2021-10-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_players_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='games',
            field=models.CharField(max_length=255),
        ),
    ]
