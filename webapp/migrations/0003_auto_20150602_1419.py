# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20150602_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('notes', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('notes', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationHistory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('notes', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_first_line',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address_second_line',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='post_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='suburb',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='work_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='address_first_line',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='address_second_line',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='country',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='post_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='state',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='suburb',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='address_first_line',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='country',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='post_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='state',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='suburb',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='address_first_line',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='country',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='post_code',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='state',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='suburb',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationhistory',
            name='organisation',
            field=models.ForeignKey(to='webapp.Organisation'),
        ),
        migrations.AddField(
            model_name='facilityhistory',
            name='facility',
            field=models.ForeignKey(to='webapp.Facility'),
        ),
        migrations.AddField(
            model_name='departmenthistory',
            name='department',
            field=models.ForeignKey(to='webapp.Department'),
        ),
    ]
