# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.core.validators
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150422_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, help_text='Enter a brief, descriptive name for the browser.', verbose_name='browser name', unique=True)),
                ('description', models.TextField(help_text='Enter a description for the browser.', verbose_name='browser description', blank=True)),
                ('slug', models.SlugField(max_length=255, help_text='Enter a unique slug for this genome browser. This should get auto-generated.', verbose_name='slug', unique=True)),
                ('chr', models.CharField(max_length=64, help_text='The chromosome to display when the browser loads.', verbose_name='default chromosome')),
                ('start', models.IntegerField(help_text='The start position of range to display when the browser loads.', validators=[django.core.validators.MinValueValidator(1)], verbose_name='default start position')),
                ('end', models.IntegerField(help_text='The end position of range to display when the browser loads.', validators=[django.core.validators.MinValueValidator(1)], verbose_name='default end position')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Genome Browsers',
                'verbose_name': 'Genome Browser',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoordSystem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('auth', models.CharField(max_length=10, help_text='Authority string used in the <a href="http://dasregistry.org/" target="_blank">DAS Registry</a>.', verbose_name='authority', blank=True)),
                ('version', models.CharField(max_length=10, help_text='Version string used in the <a href="http://dasregistry.org/" target="_blank">DAS Registry</a>.', verbose_name='version', blank=True)),
                ('ucsc_name', models.CharField(max_length=10, help_text='UCSC genome browser name of the assembly, if defined in the list of <a href="https://genome.ucsc.edu/FAQ/FAQreleases.html#release1" target="_blank">UCSC genome releases</a>.', validators=[django.core.validators.RegexValidator(regex='^[a-z]{2}\\d+$|^[a-z]{3}[A-Z][a-z]{2}\\d+$', message="UCSC name must be of the format 'gs#' or 'gggSss#'.", code='invalid_UCSC_name')], verbose_name='UCSC name', blank=True)),
            ],
            options={
                'ordering': ['species', 'auth', 'version'],
                'verbose_name_plural': 'Coordinate Systems',
                'verbose_name': 'Coordinate System',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, help_text='Enter the species name.', verbose_name='species name')),
                ('taxid', models.IntegerField(help_text='Enter the Taxonomy ID for the species. Taxonomy names and IDs can be found at <a href="http://www.ncbi.nlm.nih.gov/taxonomy" target="_blank">NCBI</a>.', null=True, verbose_name='taxonomy ID', blank=True)),
            ],
            options={
                'ordering': ['name', 'taxid'],
                'verbose_name_plural': 'Species',
                'verbose_name': 'Species',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stylesheet',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255, help_text='Enter a brief, descriptive name for this stylesheet.', verbose_name='stylesheet name', unique=True)),
                ('description', models.TextField(help_text='Describe the style this stylesheet provides.', verbose_name='stylesheet description', blank=True)),
                ('is_downloadable', models.BooleanField(help_text="Add download button for stylesheet file to the genome browser's info window.", default=True, verbose_name='stylesheet downloadable?')),
                ('style_type', models.CharField(max_length=4, help_text='Select the type of stylesheet being used.', choices=[('XML', 'DAS XML Stylesheet'), ('JSON', 'JSON-encoded Stylesheet')], verbose_name='stylesheet type')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('style_file', filer.fields.file.FilerFileField(help_text='Upload/select an image to represent this genome browser.select a stylesheet for the track. More info can be found in the <a href="https://www.biodalliance.org/stylesheets.html" target="_blank">Stylesheets for Dalliance</a> documentation.', related_name='cms_genome_browser_stylesheet_stylesheet', to='filer.File')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Stylesheets',
                'verbose_name': 'Stylesheet',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('order', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=64, help_text='Enter a brief name for the track.', verbose_name='track name')),
                ('description', models.CharField(max_length=255, help_text='Enter a short description for the track.', verbose_name='track description', blank=True)),
                ('track_type', models.CharField(max_length=20, help_text='Select the source type for this track.', choices=[('BAM', 'BAM'), ('BED', (('BED-MemStore', 'BED (MemStore)'), ('BED-Tabix', 'BED (Tabix)'))), ('bigWig', 'bigWig'), ('bigBed', 'bigBed'), ('DAS', (('DAS-feature', 'DAS (feature)'), ('DAS-sequence', 'DAS (sequence)'))), ('twoBit', 'twoBit'), ('VCF', (('VCF-MemStore', 'VCF (MemStore)'), ('VCF-Tabix', 'VCF (Tabix)'))), ('WIG', 'WIG')], verbose_name='track type')),
                ('collapse_super_groups', models.BooleanField(help_text="Attempt to allow more 'gene-like' rendering for some data sources.", default=False, verbose_name='CSG?')),
                ('provides_entrypoint', models.BooleanField(help_text='Does this track provide entry points? Entry points comprise the coordinate system on which annotations are made.', default=False, verbose_name='entry?')),
                ('pinned', models.BooleanField(help_text="'Pin' this trackc in the non-scrolling section at the top of the browser.", default=False, verbose_name='pin?')),
                ('is_downloadable', models.BooleanField(help_text="Add download button for data file to the genome browser's info window.", default=True, verbose_name='D/L?')),
                ('publish_track', models.BooleanField(help_text='Display track in the genome browser.', default=True, verbose_name='publish?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bai_file', filer.fields.file.FilerFileField(help_text="<strong>If data file is a BAM file</strong>, upload/select a BAM index (.bai) file that corresponds to the track's BAM file.", blank=True, null=True, to='filer.File', related_name='cms_genome_browser_track_bai')),
                ('browser', models.ForeignKey(help_text='Specify genome browser this track belongs to.', blank=True, null=True, to='cms_genome_browser.Browser')),
                ('data_file', filer.fields.file.FilerFileField(help_text='Upload/select a data file for the track. More info can be found in the <a href="http://www.biodalliance.org/config-source.html" target="_blank">Configuring a source</a> documentation.', related_name='cms_genome_browser_track_data', to='filer.File')),
                ('stylesheet', models.ForeignKey(help_text='Choose a stylesheet to add cusom styles to this track.', blank=True, null=True, to='cms_genome_browser.Stylesheet')),
            ],
            options={
                'ordering': ['browser', 'order'],
                'verbose_name_plural': 'Tracks',
                'verbose_name': 'Track',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coordsystem',
            name='species',
            field=models.ForeignKey(to='cms_genome_browser.Species', help_text='Select a species. Taxonomy ID is shown in parentheses, if present.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='browser',
            name='coordinate_system',
            field=models.ForeignKey(to='cms_genome_browser.CoordSystem', help_text='Select a coordinate system. Taxonomy ID, authority, version, and UCSC name are shown in parentheses, if present.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='browser',
            name='image',
            field=filer.fields.image.FilerImageField(help_text='Upload/select an image to represent this genome browser.', blank=True, null=True, to='filer.Image', related_name='cms_genome_browser_browser_browser_image'),
            preserve_default=True,
        ),
    ]
