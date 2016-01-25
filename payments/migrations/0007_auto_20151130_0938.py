# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_otp_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp_details',
            name='user',
        ),
        migrations.AddField(
            model_name='otp_details',
            name='otp_id',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]
