# Generated by Django 5.0.6 on 2024-05-21 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(max_length=200),
        ),
    ]
