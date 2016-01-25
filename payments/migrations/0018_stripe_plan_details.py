# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0017_plan_details_subscription_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='stripe_plan_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_count', models.IntegerField()),
                ('plan', models.CharField(max_length=100)),
            ],
        ),
    ]
