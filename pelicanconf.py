#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kevin Deldycke'
SITENAME = u'Kevin Deldycke'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
LOCALE = 'C'
# Don't forget to install "pip install mdx_video"
MD_EXTENSIONS = ['codehilite', 'extra', 'video']

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_DIR = 'posts'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_DIR = 'pages'

TEMPLATE_PAGES = {
    'templates/videos.html': 'video/index.html',
    'templates/code.html': 'code/index.html',
    'templates/themes.html': 'themes/index.html',
    }

# Force Pelican to use the file name as the slug, instead of derivating it from the title.
FILENAME_METADATA = '(?P<slug>.*)'

TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = False
PAGE_LANG_SAVE_AS = False

FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

#http://kevin.deldycke.com/tag/openerp/feed/
TAG_FEED_RSS = 'tag/%s/feed/index.html'
TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'

#http://example.com/category/categoryname/feed
CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'

FEED_MAX_ITEMS = 10
DEFAULT_CATEGORY = 'English'
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 5
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False

THEME = "plumage"

STATIC_PATHS = [
    'uploads',
    'documents',
    ]

FILES_TO_COPY = (
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/robots.txt', 'robots.txt'),
    ('extra/htaccess', '.htaccess'),
    ('extra/htaccess-static', 'static/.htaccess'),
    )

PLUGIN_PATH = 'plugins'
PLUGINS = [
    'related_posts',
    'neighbors',
    'sitemap',
    ]


### Plugin-specific settings

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


### Theme-specific settings

SITE_THUMBNAIL = '/static/uploads/2006/avatar-orig.png'
SITE_THUMBNAIL_TEXT = 'Official avatar since MMIV'

SITESUBTITLE = "Open-Source Software Engineer"

MENUITEMS = (
    ('Home', '/'),
    ('Videos', '/video/'),
    ('Code', '/code/'),
    ('Themes', '/themes/'),
    ('About', '/about/'),
    )

GOOGLE_SEARCH = 'partner-pub-0142056597033291:1880158713'

LEFT_SIDEBAR = """
    <!--<div data-spy="affix" data-offset-top="0">-->
    <!--<h4>Sponsors</h4>-->
    <script type="text/javascript"><!--
      google_ad_client = "pub-0142056597033291";
      google_ad_slot = "9501596707";
      google_ad_width = 160;
      google_ad_height = 600;
      //-->
    </script>
    <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
    <!--</div>-->
    """

ARTICLE_EDIT_LINK = 'https://github.com/kdeldycke/kevin-deldycke-blog/edit/master/content/posts/%(slug)s.md'

SOCIAL_TITLE = "Contact"
SOCIAL = (
    ('@kdeldycke', 'http://twitter.com/kdeldycke'),
    ('kevin@deldycke.com', 'mailto:kevin@deldycke.com'),
    )

LINKS_TITLE = "Professional profiles"
LINKS = (
    ('PDF resume', 'http://docs.google.com/document/export?format=pdf&amp;id=1XaJgwRAhxHDuBSD-JqE--8WKGx0uTasa6IOU4IFBeKg'),
    ('Careers 2.0', 'http://careers.stackoverflow.com/kdeldycke'),
    ('LinkedIn', 'http://linkedin.com/in/kevindeldycke/en'),
    ('Viadeo', 'http://viadeo.com/fr/profile/kevin.deldycke'),
    )

COPYRIGHT = "Unless contrary mention, the licensing terms below applies:<br/>Code and software released under <a href='http://www.fsf.org/licensing/licenses/gpl.html'>GNU/GPL licence v2.0</a>;<br/>Other content published under <a href='http://creativecommons.org/licenses/by-sa/3.0/'>Creative Commons Attribution-Share Alike 3.0 license</a>."

DISQUS_SITENAME = 'kevin-deldycke-blog'
GOOGLE_ANALYTICS = 'UA-657524-1'
GOOGLE_ANALYTICS_DOMAIN = 'deldycke.com'
