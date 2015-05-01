# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150422_1656'),
        ('cms_genome_browser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='bai_file',
        ),
        migrations.AddField(
            model_name='track',
            name='index_file',
            field=filer.fields.file.FilerFileField(null=True, to='filer.File', blank=True, help_text="<strong>If data file is a BAM or Tabix file</strong>, upload/select an index file (.bai or .tbi) that corresponds to the track's BAM/Tabix file.", related_name='cms_genome_browser_track_index'),
            preserve_default=True,
        ),
    ]
