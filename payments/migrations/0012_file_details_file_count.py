# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0011_auto_20151201_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_details',
            name='file_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
