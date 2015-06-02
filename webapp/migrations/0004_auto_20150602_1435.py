# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20150602_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departmenthistory',
            options={'verbose_name_plural': 'Department History'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='facilityhistory',
            options={'verbose_name_plural': 'Facility History'},
        ),
        migrations.AlterModelOptions(
            name='organisationhistory',
            options={'verbose_name_plural': 'Organisation History'},
        ),
        migrations.AlterField(
            model_name='department',
            name='contacts',
            field=models.ManyToManyField(to='webapp.Contact', blank=True),
        ),
        migrations.AlterField(
            model_name='departmenthistory',
            name='department',
            field=models.ForeignKey(to='webapp.Department', blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='contacts',
            field=models.ManyToManyField(to='webapp.Contact', blank=True),
        ),
        migrations.AlterField(
            model_name='facilityhistory',
            name='facility',
            field=models.ForeignKey(to='webapp.Facility', blank=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='contacts',
            field=models.ManyToManyField(to='webapp.Contact', blank=True),
        ),
        migrations.AlterField(
            model_name='organisationhistory',
            name='organisation',
            field=models.ForeignKey(to='webapp.Organisation', blank=True),
        ),
    ]
