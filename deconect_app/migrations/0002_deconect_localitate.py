# Generated by Django 3.0.5 on 2021-03-24 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deconect_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deconect',
            name='localitate',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
