# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-28 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('specialuseform', '0010_auto_20160928_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_address_1',
            field=models.CharField(blank=True, max_length=250, verbose_name='Street Address 1'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_address_2',
            field=models.CharField(blank=True, help_text='(Optional)', max_length=250, verbose_name='Street Address 2'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_city',
            field=models.CharField(blank=True, max_length=250, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_name',
            field=models.CharField(default='Additional Permit Holder', help_text='Name of Permit Holder', max_length=250),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_signature',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_state',
            field=localflavor.us.models.USStateField(blank=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_zipcode',
            field=localflavor.us.models.USZipCodeField(blank=True, verbose_name='Zipcode'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_address_1',
            field=models.CharField(default='use organizer', max_length=250, verbose_name='Street Address 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_address_2',
            field=models.CharField(blank=True, help_text='(Optional)', max_length=250, verbose_name='Street Address 2'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_city',
            field=models.CharField(default='use organizer', max_length=250, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_state',
            field=localflavor.us.models.USStateField(default='use organizer', verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_zipcode',
            field=localflavor.us.models.USZipCodeField(default='use organizer', verbose_name='Zipcode'),
            preserve_default=False,
        ),
    ]
