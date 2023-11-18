# Generated by Django 4.2.6 on 2023-11-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_movie_poster'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_movie', to='catalog.movie'),
        ),
    ]