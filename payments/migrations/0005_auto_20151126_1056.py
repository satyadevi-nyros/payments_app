# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_auto_20151126_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile_details',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user_details',
        ),
    ]
