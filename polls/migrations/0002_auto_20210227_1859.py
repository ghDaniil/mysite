# Generated by Django 3.1.6 on 2021-02-27 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='c_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
