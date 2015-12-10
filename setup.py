import os
import sys
from setuptools import setup

if sys.version_info < (3, 2):
    print("Sorry, djangocms-genome-browser currently requires Python 3.2+.")
    sys.exit(1)

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'Django>=1.7',
    'django-cms>=3.0.7,<3.2',
    'django-filer>=0.9.10',
]

setup(
    name='djangocms-genome-browser',
    version='0.1.1',
    packages=['cms_genome_browser'],
    include_package_data=True,
    license='BSD License',
    description='A Django app for incorporating a Dalliance genome browser into a Django site with django CMS-specific features',
    long_description=README,
    url='https://github.com/mfcovington/djangocms-genome-browser',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    install_requires=install_requires,
)
