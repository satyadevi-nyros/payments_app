# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_plan_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan_details',
            name='subscription_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
