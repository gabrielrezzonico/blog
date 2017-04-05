#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gabriel Rezzonico'
SITENAME = 'Machine Leaning and Programming'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'

THEME = 'themes/pelican-clean-blog'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

## THEME

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/gabrielrezzonico/'),
          ('github', 'https://github.com/gabrielrezzonico/'),
          ('facebook','https://www.facebook.com/gabrielrezzonico'),
          ('envelope','mailto:gabrielrezzonico@gmail.com'))