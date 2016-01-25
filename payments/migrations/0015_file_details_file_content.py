# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0014_mobile_details_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_details',
            name='file_content',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]
