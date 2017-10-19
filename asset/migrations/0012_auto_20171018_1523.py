# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0011_auto_20171018_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='eth0',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡1mac地址'),
        ),
        migrations.AddField(
            model_name='asset',
            name='eth1',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡2mac地址'),
        ),
        migrations.AddField(
            model_name='asset',
            name='eth2',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡3mac地址'),
        ),
        migrations.AddField(
            model_name='asset',
            name='eth3',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡4mac地址'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='%Y%m%d46667'),
        ),
    ]