# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-02 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('other_details', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('price', models.FloatField(default=0)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
            ],
        ),
        migrations.CreateModel(
            name='purchase_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.purchase')),
            ],
        ),
    ]