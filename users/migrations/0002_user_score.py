# Generated by Django 3.2.3 on 2021-05-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
