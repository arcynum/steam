# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20150602_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='post_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
