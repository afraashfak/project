# Generated by Django 3.2.7 on 2021-10-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
