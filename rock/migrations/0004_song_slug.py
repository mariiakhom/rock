# Generated by Django 4.2 on 2023-05-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0003_group_member7'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
