AUTHOR = 'cycletux'
SITENAME = "Cycletux' Blog"
SITEURL = 'https://www.cycletux.de/pelican'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'
THEME = "pelican-themes/notmyidea-cms"

PLUGINS = [] #'image_process']


DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

# IMAGE_PROCESS = {
#     "article-image": [], #"scale_in 600 600 True"],
#     "thumb": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
# }


# Social widget
SOCIAL = (('Mastodon', 'https://sueden.social/@cycletux'),)

DEFAULT_PAGINATION = False
HIDE_CATEGORIES_FROM_MENU = False
MENUITEMS = (('Blog', '/'),)

SUMMARY_MAX_LENGTH = 50
SUMMARY_END_SUFFIX = "..."
READ_MORE_LINK = '<span>continue</span>'
READ_MORE_LINK_FORMAT = '<a class="read-more" href="/{url}">{text}</a>'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
