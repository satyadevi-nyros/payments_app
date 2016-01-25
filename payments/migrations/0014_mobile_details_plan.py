# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0013_auto_20151201_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile_details',
            name='plan',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
