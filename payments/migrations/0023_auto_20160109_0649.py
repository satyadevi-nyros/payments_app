# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0022_auto_20160109_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepic',
            name='model_pic',
            field=models.ImageField(null=True, upload_to=b'satya', blank=True),
        ),
    ]
