# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_log', '0006_auto_20190816_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='user_id',
            field=models.CharField(verbose_name='user id ', max_length=32),
        ),
    ]
