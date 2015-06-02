# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('home_phone', models.IntegerField()),
                ('work_phone', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('notes', models.TextField()),
                ('address_first_line', models.CharField(max_length=255)),
                ('address_second_line', models.CharField(max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('address_first_line', models.CharField(max_length=255)),
                ('address_second_line', models.CharField(max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('contacts', models.ManyToManyField(to='webapp.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('address_first_line', models.CharField(max_length=255)),
                ('address_second_line', models.CharField(blank=True, max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('contacts', models.ManyToManyField(to='webapp.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('address_first_line', models.CharField(max_length=255)),
                ('address_second_line', models.CharField(blank=True, max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('post_code', models.IntegerField()),
                ('contacts', models.ManyToManyField(to='webapp.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='organisation',
            field=models.ForeignKey(to='webapp.Organisation'),
        ),
        migrations.AddField(
            model_name='department',
            name='facility',
            field=models.ForeignKey(to='webapp.Facility'),
        ),
    ]
