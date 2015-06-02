# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20150602_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='type',
        ),
    ]
