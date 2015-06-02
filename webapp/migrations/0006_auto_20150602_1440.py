# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20150602_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_phone',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_phone',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='post_code',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='post_code',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
