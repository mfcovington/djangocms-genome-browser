from django.contrib import admin
from cms_genome_browser.models import Browser, CoordSystem, Species, Stylesheet, Track

class TrackInline(admin.TabularInline):
    model = Track
    extra = 2


class BrowserAdmin(admin.ModelAdmin):

    fieldset_browser = ('Genome browser', {
        'fields': [
            'name',
            'description',
            'image',
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

    inlines = [
        TrackInline,
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


class StylesheetAdmin(admin.ModelAdmin):

    fieldset_basic = ('Basic Info', {
        'fields': [
            'name',
            'description',
        ],
    })

    fieldset_content = ('Stylesheet Content', {
        'fields': [
            'style_file',
            'style_type',
            'is_downloadable',
        ],
    })

    fieldsets = [
        fieldset_basic,
        fieldset_content,
    ]

    list_display = (
        'name',
        'style_file',
        'style_type',
        'is_downloadable',
    )
    list_filter = (
        'style_type',
        'is_downloadable',
    )
    search_fields = (
        'description',
        'name',
        'style_file',
    )

admin.site.register(Stylesheet, StylesheetAdmin)


class TrackAdmin(admin.ModelAdmin):

    fieldset_basic = ('Basic Info', {
        'fields': [
            'name',
            'description',
            'publish_track',
        ],
    })

    fieldset_browser = ('Genome browser', {
        'fields': [
            'browser',
            'order',
        ],
    })

    fieldset_content = ('Track Content', {
        'fields': [
            'track_type',
            'data_file',
            'index_file',
            'stylesheet',
            'is_downloadable',
        ],
    })

    fieldset_advanced = ('Advanced Settings', {
        'fields': [
            'collapse_super_groups',
            'provides_entrypoint',
            'pinned',
        ],
    })

    fieldsets = [
        fieldset_basic,
        fieldset_browser,
        fieldset_content,
        fieldset_advanced,
    ]

    list_display = (
        'name',
        'track_type',
        'data_file',
        'stylesheet',
        'browser',
        'order',
        'collapse_super_groups',
        'provides_entrypoint',
        'pinned',
        'is_downloadable',
        'publish_track',
    )
    list_filter = (
        'track_type',
        'browser',
        'collapse_super_groups',
        'provides_entrypoint',
        'pinned',
        'is_downloadable',
        'publish_track',
    )
    search_fields = (
        'data_file',
        'description',
        'name',
        'stylesheet',
    )

admin.site.register(Track, TrackAdmin)
