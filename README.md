# Dalliance Genome Browser + Django

CMS Genome Browser is A Django app for incorporating a [Dalliance genome browser(https://github.com/dasmoth/dalliance) into a Django site with django CMS-specific features.

<!-- Detailed documentation is in the "docs" directory. -->

## Quick start

- Edit the project's `settings.py` file.

    - Add `cms_genome_browser` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'cms_genome_browser',
            'easy_thumbnails',
            'filer',
            'mptt',
        )
        ```

    - Specify your media settings, if not already specified:

        ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

    - Add `filer` and `easy_thumbnail` settings: 

        ```python
        # For filer's Django 1.7 compatibility
        MIGRATION_MODULES = {
            ...
            'filer': 'filer.migrations_django',
        }

        # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
        THUMBNAIL_HIGH_RESOLUTION = True
        THUMBNAIL_QUALITY = 95
        THUMBNAIL_PROCESSORS = (
            'easy_thumbnails.processors.colorspace',
            'easy_thumbnails.processors.autocrop',
            'filer.thumbnail_processors.scale_and_crop_with_subject_location',
            'easy_thumbnails.processors.filters',
        )
        THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
        THUMBNAIL_SUBDIR = 'versions'
        ```

- Include URL configurations for `cms_genome_browser` in your project's `urls.py` file:

    ```python
    urlpatterns = patterns('',
        ...
        url(r'^genome_browser/', include('cms_genome_browser.urls', namespace='cms_genome_browser')),
        ...
    )
    ```

- Run `python manage.py makemigrations cms_genome_browser` to create the cms_genome_browser migrations.

- Run `python manage.py migrate` to create the cms_genome_browser models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and attach the `Genome Browser App` under `Advanced Settings` for the page.

*Version 0.1.1*
