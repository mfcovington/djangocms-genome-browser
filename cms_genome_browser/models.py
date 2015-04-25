from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

class Browser(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = "Genome Browser"
        verbose_name_plural = "Genome Browsers"

    name = models.CharField('browser name',
        help_text='Enter a brief, descriptive name for the browser.',
        max_length=255,
        unique=True,
    )

    description = models.TextField('browser description',
        blank=True,
        help_text='Enter a description for the browser.',
    )

    image = FilerImageField(
        blank=True,
        null=True,
        help_text='Upload/select an image to represent this genome browser.',
        related_name='%(app_label)s_%(class)s_browser_image',
    )

    slug = models.SlugField('slug',
        help_text='Enter a unique slug for this genome browser. ' \
                  'This should get auto-generated.',
        max_length=255,
        unique=True,
    )

    chr = models.CharField('default chromosome',
        help_text='The chromosome to display when the browser loads.',
        max_length=64,
    )

    start = models.IntegerField('default start position',
        help_text='The start position of range to display when the browser loads.',
        validators=[
            MinValueValidator(1),
        ],
    )

    end = models.IntegerField('default end position',
        help_text='The end position of range to display when the browser loads.',
        validators=[
            MinValueValidator(1),
        ],
    )

    coordinate_system = models.ForeignKey('cms_genome_browser.CoordSystem',
        help_text='Select a coordinate system. Taxonomy ID, authority, version, ' \
                  'and UCSC name are shown in parentheses, if present.',
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.start > self.end:
            raise ValidationError('Start position cannot come after end position.')

    def __str__(self):
        return self.name


class CoordSystem(models.Model):

    class Meta:
        ordering = ['species', 'auth', 'version']
        verbose_name = "Coordinate System"
        verbose_name_plural = "Coordinate Systems"

    UCSC_OLD_REGEX = r'^[a-z]{2}\d+$'                 # gs#
    UCSC_NEW_REGEX = r'^[a-z]{3}[A-Z][a-z]{2}\d+$'    # gggSss#

    species = models.ForeignKey('cms_genome_browser.Species',
        help_text='Select a species. Taxonomy ID is shown in parentheses, if present.',
    )

    auth = models.CharField('authority',
        blank=True,
        help_text='Authority string used in the ' \
                  '<a href="http://dasregistry.org/" target="_blank">DAS Registry</a>.',
        max_length=10,
    )

    version = models.CharField('version',
        blank=True,
        help_text='Version string used in the ' \
                  '<a href="http://dasregistry.org/" target="_blank">DAS Registry</a>.',
        max_length=10,
    )

    ucsc_name = models.CharField('UCSC name',
        blank=True,
        help_text='UCSC genome browser name of the assembly, if defined in the list of ' \
                  '<a href="https://genome.ucsc.edu/FAQ/FAQreleases.html#release1" target="_blank">' \
                  'UCSC genome releases</a>.',
        max_length=10,
        validators=[
            RegexValidator(
                regex='%s|%s' % (UCSC_OLD_REGEX, UCSC_NEW_REGEX),
                message="UCSC name must be of the format 'gs#' or 'gggSss#'.",
                code='invalid_UCSC_name'
            ),
        ]
    )

    def __str__(self):
        coord_system_str = self.species.name
        supplemental = []

        if self.species.taxid:
            supplemental.append(str(self.species.taxid))

        supplemental.append(' '.join([self.auth, self.version]))

        if self.ucsc_name:
            supplemental.append(self.ucsc_name)

        if supplemental:
            coord_system_str += ' (%s)' % '; '.join(supplemental)
        return coord_system_str


class Species(models.Model):

    class Meta:
        ordering = ['name', 'taxid']
        verbose_name = "Species"
        verbose_name_plural = "Species"

    name = models.CharField('species name',
        help_text='Enter the species name.',
        max_length=255,
    )

    taxid = models.IntegerField('taxonomy ID',
        blank=True,
        null=True,
        help_text='Enter the Taxonomy ID for the species. ' \
                  'Taxonomy names and IDs can be found at ' \
                  '<a href="http://www.ncbi.nlm.nih.gov/taxonomy" target="_blank">NCBI</a>.',
    )

    def __str__(self):
        species_str = self.name
        if self.taxid:
            species_str += ' (%s)' % self.taxid
        return species_str


class Stylesheet(models.Model):

    class Meta:
        ordering = ['name',]
        verbose_name='Stylesheet'
        verbose_name_plural='Stylesheets'

    STYLESHEET_TYPE_CHOICES = (
        ('XML', 'DAS XML Stylesheet'),
        ('JSON', 'JSON-encoded Stylesheet'),
    )

    name = models.CharField('stylesheet name',
        help_text='Enter a brief, descriptive name for this stylesheet.',
        max_length=255,
        unique=True,
    )

    description = models.TextField('stylesheet description',
        blank=True,
        help_text='Describe the style this stylesheet provides.',
    )

    style_file = FilerFileField(
        help_text='Upload/select an image to represent this genome browser.select a stylesheet for the track. More info can be found in the ' \
                  '<a href="https://www.biodalliance.org/stylesheets.html" target="_blank">' \
                  'Stylesheets for Dalliance</a> documentation.',
        related_name='%(app_label)s_%(class)s_stylesheet',
    )

    is_downloadable = models.BooleanField('stylesheet downloadable?',
        default=True,
        help_text="Add download button for stylesheet file to the genome browser's info window.",
    )

    style_type = models.CharField('stylesheet type',
        choices=STYLESHEET_TYPE_CHOICES,
        help_text='Select the type of stylesheet being used.',
        max_length=4,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
