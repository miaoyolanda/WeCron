# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('openid', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('subscribe', models.NullBooleanField(choices=[(0, '\u672a\u5b9a\u9605'), (1, '\u5df2\u8ba2\u9605')], verbose_name='\u662f\u5426\u8ba2\u9605')),
                ('nickname', models.CharField(max_length=40, null=True, verbose_name='\u6635\u79f0')),
                ('sex', models.SmallIntegerField(choices=[(0, '\u672a\u77e5'), (1, '\u7537\u6027'), (2, '\u5973\u6027')], null=True, verbose_name='\u6027\u522b')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='\u57ce\u5e02')),
                ('country', models.CharField(max_length=100, null=True, verbose_name='\u56fd\u5bb6')),
                ('province', models.CharField(max_length=100, null=True, verbose_name='\u7701\u4efd')),
                ('language', models.CharField(max_length=50, null=True, verbose_name='\u8bed\u8a00')),
                ('headimgurl', models.CharField(max_length=200, null=True, verbose_name='\u5934\u50cf\u5730\u5740')),
                ('subscribe_time', models.IntegerField(null=True, verbose_name='\u5173\u6ce8\u65f6\u95f4')),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8')),
                ('groupid', models.IntegerField(null=True, verbose_name='\u5206\u7ec4ID')),
            ],
            options={
                'ordering': ['-subscribe_time'],
                'db_table': 'user',
            },
        ),
    ]