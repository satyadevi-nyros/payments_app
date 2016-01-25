# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_auto_20151130_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp_details',
            name='otp_password',
            field=models.CharField(max_length=200),
        ),
    ]
