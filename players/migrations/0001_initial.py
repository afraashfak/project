# Generated by Django 3.2.7 on 2021-10-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=255)),
                ('playeremail', models.CharField(max_length=255)),
                ('country', models.IntegerField()),
                ('games', models.IntegerField()),
                ('score', models.FloatField()),
            ],
        ),
    ]