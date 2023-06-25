# Generated by Django 4.2 on 2023-05-30 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rock', '0007_alter_comment_options_song_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='wishing_to_listen',
            field=models.ManyToManyField(blank=True, related_name='playlist', to=settings.AUTH_USER_MODEL),
        ),
    ]