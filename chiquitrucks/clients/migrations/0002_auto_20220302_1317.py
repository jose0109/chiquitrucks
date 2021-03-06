# Generated by Django 3.2.5 on 2022-03-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='personal_id',
            field=models.IntegerField(unique=True),
        ),
    ]
