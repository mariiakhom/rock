# Generated by Django 4.2 on 2023-05-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='trailer',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
