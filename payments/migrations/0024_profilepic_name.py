# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0023_auto_20160109_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilepic',
            name='Name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
