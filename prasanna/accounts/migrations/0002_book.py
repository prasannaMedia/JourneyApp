# Generated by Django 3.0.5 on 2020-04-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=30)),
                ('userid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('busid', models.DecimalField(decimal_places=0, max_digits=2)),
                ('bus_name', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], default='B', max_length=2)),
            ],
        ),
    ]