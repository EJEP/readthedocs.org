# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-12 13:05
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0010_add-sold-clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporterpromo',
            name='theme',
            field=models.CharField(blank=True, choices=[(b'any', b'Any'), (b'alabaster', b'Alabaster Theme'), (b'sphinx_rtd_theme', b'Read the Docs Sphinx Theme')], default=b'sphinx_rtd_theme', max_length=40, null=True, verbose_name='Theme'),
        ),
    ]
