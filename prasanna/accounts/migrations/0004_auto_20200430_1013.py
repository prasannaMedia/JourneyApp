# Generated by Django 3.0.5 on 2020-04-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200428_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='status',
        ),
        migrations.AlterField(
            model_name='book',
            name='busid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='nos',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='userid',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.CharField(max_length=30),
        ),
    ]
