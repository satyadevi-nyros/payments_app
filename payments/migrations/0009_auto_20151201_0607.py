# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_auto_20151130_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='file_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('file_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='mobile_details',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
