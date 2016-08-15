# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-15 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkbookFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='sheet_uploads/', verbose_name='Path to Spreadsheet')),
                ('file_hash', models.TextField(editable=False, max_length=256, unique=True)),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Date Uploaded')),
            ],
        ),
        migrations.RenameModel(
            old_name='SheetEntry',
            new_name='WorkbookEntry',
        ),
        migrations.DeleteModel(
            name='SheetFile',
        ),
    ]
