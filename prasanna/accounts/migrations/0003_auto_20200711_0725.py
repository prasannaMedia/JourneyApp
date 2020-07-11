# Generated by Django 3.0.5 on 2020-07-11 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200709_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cost',
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='busid',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='nos',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='book',
            name='userid',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bus',
            name='nos',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='bus',
            name='rem',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
