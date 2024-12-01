AUTHOR = 'JJW'
SITENAME = 'SPIN J'
SITEURL = ""

PATH = "content"
OUTPUT_PATH = 'docs'
STATIC_PATHS = ['.']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SLUGIFY_SOURCE = 'basename'
# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "./themes/blue-penguin-dark-master"
