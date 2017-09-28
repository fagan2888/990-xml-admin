# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-23 20:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='known_version_string',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_string', models.CharField(blank=True, max_length=15, null=True)),
                ('num_observed', models.IntegerField(blank=True, help_text='Index file year', null=True)),
                ('max_year', models.IntegerField(blank=True, help_text='max index file year', null=True)),
                ('min_year', models.IntegerField(blank=True, help_text='min index file year', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='master_observed_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_xpath', models.CharField(blank=True, max_length=511, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='master_observed_xpath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_xpath', models.CharField(blank=True, max_length=511, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='observed_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_file_year', models.IntegerField(blank=True, help_text='Index file year', null=True)),
                ('version_string', models.CharField(blank=True, max_length=15, null=True)),
                ('raw_xpath', models.CharField(blank=True, max_length=511, null=True)),
                ('num_observed', models.IntegerField(blank=True, help_text='Index file year', null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('master_xpath', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filing.master_observed_group')),
            ],
        ),
        migrations.CreateModel(
            name='observed_xpath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_file_year', models.IntegerField(blank=True, help_text='Index file year', null=True)),
                ('version_string', models.CharField(blank=True, max_length=15, null=True)),
                ('raw_xpath', models.CharField(blank=True, max_length=511, null=True)),
                ('num_observed', models.IntegerField(blank=True, help_text='Index file year', null=True)),
                ('last_update', models.DateTimeField(auto_now=True, null=True)),
                ('observed_type', models.CharField(blank=True, help_text='character representation of data type, as observed', max_length=511, null=True)),
                ('containing_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filing.observed_group')),
                ('master_xpath', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='filing.master_observed_xpath')),
            ],
        ),
        migrations.CreateModel(
            name='xml_submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, help_text='Index file year', null=True)),
                ('return_id', models.CharField(blank=True, db_index=True, help_text="IRS' unique id, so index this", max_length=31, null=True)),
                ('filing_type', models.CharField(blank=True, help_text='probably EFILE', max_length=15, null=True)),
                ('ein', models.CharField(help_text='employee id number', max_length=15)),
                ('tax_period', models.IntegerField(blank=True, help_text='Filing month YYYYMM', null=True)),
                ('sub_date', models.CharField(blank=True, help_text='submitted date: YYYY-MM-DD', max_length=511, null=True)),
                ('taxpayer_name', models.CharField(blank=True, max_length=511, null=True)),
                ('return_type', models.CharField(blank=True, max_length=7, null=True)),
                ('dln', models.CharField(blank=True, max_length=31, null=True)),
                ('object_id', models.CharField(blank=True, max_length=31, null=True)),
                ('as_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('schema_year', models.IntegerField(blank=True, help_text='Schema year', null=True)),
                ('schema_version', models.TextField(help_text='Schema version', null=True)),
                ('json_set', models.BooleanField(default=False, help_text='Has the json been set?')),
            ],
            options={
                'verbose_name': 'XML Submission',
                'managed': True,
            },
        ),
    ]
