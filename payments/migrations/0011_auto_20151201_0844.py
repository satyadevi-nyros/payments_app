# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_file_details_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_details',
            name='file_name',
            field=models.FileField(upload_to=b''),
        ),
    ]
