# Generated by Django 3.2.5 on 2022-02-28 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='modified',
        ),
    ]
