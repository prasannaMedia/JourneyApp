# Generated by Django 3.0.5 on 2020-04-28 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='bus',
            name='nos',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='bus',
            name='rem',
            field=models.CharField(max_length=30),
        ),
    ]