AUTHOR = 'JJW'
SITENAME = 'JJW website'
SITEURL = ""

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
PATH = "content-en"
OUTPUT_PATH = 'docs'
THEME = "./themes/blue-penguin-dark-master-en"

URL_PRE = 'en-'
# OUTPUT_PATH = 'output/en'
INDEX_SAVE_AS = URL_PRE + 'index.html'
ARCHIVES_SAVE_AS = URL_PRE + 'archives.html'
AUTHORS_SAVE_AS = URL_PRE + 'authors.html'
CATEGORIES_SAVE_AS = URL_PRE + 'categories.html'
TAGS_SAVE_AS = URL_PRE + 'tags.html'
ARTICLE_URL = URL_PRE + "{slug}.html"
ARTICLE_SAVE_AS = URL_PRE + "{slug}.html"
PAGE_URL = URL_PRE + 'pages/{slug}'
PAGE_SAVE_AS = URL_PRE + 'pages/{slug}.html'

SLUGIFY_SOURCE = 'basename'
# DEFAULT_CATEGORY = '未分类'
DISPLAY_CATEGORIES_ON_MENU = True
# MENUITEMS = [('首页', '/'),
#              ('分类', '/categories.html'),
#              ('标签', '/tags.html')
#              ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
