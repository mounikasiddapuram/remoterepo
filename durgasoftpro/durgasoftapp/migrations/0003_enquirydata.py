# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-27 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('durgasoftapp', '0002_feedbackdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('courses', multiselectfield.db.fields.MultiSelectField(choices=[('Py', 'Python'), ('Dj', 'Django'), ('RA', 'REST API'), ('Fl', 'Flask'), ('UI', 'UI')], max_length=14)),
                ('shifts', multiselectfield.db.fields.MultiSelectField(choices=[('morning', 'Morning Shift'), ('Afternoon', 'Afternoon Shift'), ('Evening', 'Evening Shift'), ('Night', 'Night Shift')], max_length=31)),
                ('start_date', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
