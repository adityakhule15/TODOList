# Generated by Django 4.0.5 on 2022-06-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=500)),
                ('LastName', models.CharField(max_length=500)),
                ('Email', models.CharField(max_length=500)),
                ('IsActive', models.CharField(max_length=500)),
                ('Roles', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TODOIList',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
    ]
