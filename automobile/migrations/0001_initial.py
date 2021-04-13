# Generated by Django 3.1.7 on 2021-03-31 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name='year')),
                ('discounted_price', models.IntegerField()),
                ('actual_price', models.IntegerField()),
                ('description', models.TextField()),
                ('car_photo1', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('car_photo2', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('car_photo3', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('car_photo4', models.ImageField(upload_to='photo/%Y/%m/%d')),
                ('milage', models.IntegerField()),
                ('brand', models.CharField(choices=[('BMW', 'BMW'), ('Mercedez', 'Mercedez'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Nissan', 'Nissan'), ('Audi', 'Audi')], max_length=50)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=50)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
