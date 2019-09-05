# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-04 07:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='设施名称')),
            ],
            options={
                'verbose_name': '设施信息',
                'verbose_name_plural': '设施信息',
                'db_table': 'ih_facility_info',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=64, verbose_name='房屋标题')),
                ('price', models.IntegerField(default=0, verbose_name='房屋单价')),
                ('address', models.CharField(default='', max_length=512, verbose_name='房屋地址')),
                ('room_count', models.SmallIntegerField(default=1, verbose_name='房间数目')),
                ('acreage', models.IntegerField(default=0, verbose_name='房屋面积')),
                ('unit', models.CharField(default='', max_length=32, verbose_name='房屋单元')),
                ('capacity', models.SmallIntegerField(default=1, verbose_name='房屋容纳')),
                ('beds', models.CharField(default='', max_length=64, verbose_name='房屋床铺配置')),
                ('deposit', models.IntegerField(default=0, verbose_name='房屋押金')),
                ('min_days', models.SmallIntegerField(default=1, verbose_name='最少入住天数')),
                ('max_days', models.SmallIntegerField(default=0, verbose_name='最大入住天数')),
                ('order_count', models.IntegerField(default=0, verbose_name='预计该房屋的订单数')),
                ('index_image_url', models.CharField(default='', max_length=500, verbose_name='房屋主图片的路径')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Area', verbose_name='房屋地区')),
                ('facilities', models.ManyToManyField(to='house.Facility')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='房屋用户')),
            ],
            options={
                'verbose_name': '房屋信息',
                'verbose_name_plural': '房屋信息',
                'db_table': 'ih_house_info',
            },
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('url', models.CharField(max_length=256, verbose_name='房屋图片地址')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House', verbose_name='房屋信息')),
            ],
            options={
                'verbose_name': '房屋图片',
                'verbose_name_plural': '房屋图片',
                'db_table': 'ih_house_image',
            },
        ),
    ]
