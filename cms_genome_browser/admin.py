from django.contrib import admin
from cms_genome_browser.models import Browser, CoordSystem, Species

class BrowserAdmin(admin.ModelAdmin):

    fieldset_browser = ('Genome browser', {
        'fields': [
            'name',
            'coordinate_system',
        ],
    })

    fieldset_default_range = ('Default Range', {
        'fields': [
            'chr',
            'start',
            'end',
        ],
    })

    fieldset_advanced = ('Advanced', {
        'fields': [
            'slug',
        ],
        'classes': [
            'collapse',
        ],
    })

    fieldsets = [
        fieldset_browser,
        fieldset_default_range,
        fieldset_advanced,
    ]

    list_display = (
        'name',
        'coordinate_system',
    )
    list_filter = (
        'coordinate_system__species__name',
        'coordinate_system__auth',
        'coordinate_system__ucsc_name',
    )
    search_fields = (
        'name',
        'coordinate_system__species__name',
        'coordinate_system__species__taxid',
        'coordinate_system__auth',
        'coordinate_system__version',
        'coordinate_system__ucsc_name',
    )

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Browser, BrowserAdmin)


class CoordSystemAdmin(admin.ModelAdmin):

    list_display = (
        'species',
        'auth',
        'version',
        'ucsc_name',
    )
    list_filter = (
        'species__name',
        'auth',
        'ucsc_name',
    )
    search_fields = (
        'species__name',
        'species__taxid',
        'auth',
        'version',
        'ucsc_name',
    )

admin.site.register(CoordSystem, CoordSystemAdmin)


class SpeciesAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'taxid',
    )
    list_filter = (
        'name',
    )
    search_fields = (
        'name',
        'taxid',
    )

admin.site.register(Species, SpeciesAdmin)
