# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 42, 37, 344386, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 42, 44, 813184, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 42, 53, 156987, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 42, 56, 641384, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 42, 59, 578903, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 1, 391415, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facility',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 2, 782049, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facility',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 4, 610185, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 6, 594573, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 9, 47714, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 10, 969601, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 12, 610237, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 14, 625875, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 16, 438386, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workorder',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 18, 282148, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workorder',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 3, 43, 21, 516544, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
