# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-21 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('permit_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=250)),
                ('organizer_address_1', models.CharField(max_length=250)),
                ('organizer_address_2', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('state', localflavor.us.models.USStateField(default='OH')),
                ('zipcode', localflavor.us.models.USZipCodeField()),
                ('phone_daytime', localflavor.us.models.PhoneNumberField(blank=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=250)),
                ('participant_number', models.IntegerField()),
                ('spectator_number', models.IntegerField(blank=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('organizer_name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('needs_approval', 'Needs Approval'), ('approved', 'Approved'), ('in_review', 'In Review'), ('not_approved', 'Not Approved')], default='needs_approval', max_length=10)),
            ],
        ),
    ]
