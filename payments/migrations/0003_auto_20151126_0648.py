# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_mobile_details_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_details',
            name='mobile_number',
            field=models.IntegerField(unique=True),
        ),
    ]
