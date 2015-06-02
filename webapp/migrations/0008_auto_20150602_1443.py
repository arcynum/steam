# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_contact_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='post_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
