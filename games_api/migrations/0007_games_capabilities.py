# Generated by Django 4.0.2 on 2022-02-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_api', '0006_alter_games_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='capabilities',
            field=models.ManyToManyField(to='games_api.Capabilities'),
        ),
    ]
