# Generated by Django 4.0.5 on 2022-06-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoilist',
            name='Description',
            field=models.CharField(max_length=2000),
        ),
    ]
