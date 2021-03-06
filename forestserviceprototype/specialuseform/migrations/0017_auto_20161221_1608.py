# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialuseform', '0016_auto_20161215_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='spectator_number',
            field=models.IntegerField(blank=True, help_text='If your event will have spectators (such as at a sporting event), please note how many additional people will be spectators', null=True, verbose_name='Number of Spectators'),
        ),
    ]
