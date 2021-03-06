# Generated by Django 3.1.6 on 2021-03-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210227_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(default='', max_length=500),
        ),
    ]
