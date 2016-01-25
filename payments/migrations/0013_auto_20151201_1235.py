# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_file_details_file_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_details',
            name='file_count',
        ),
        migrations.AddField(
            model_name='mobile_details',
            name='file_count',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
