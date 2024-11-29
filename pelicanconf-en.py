import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITENAME = 'Quantum JJW'

DEFAULT_LANG = 'en'
PATH = "content-en"
THEME = "./themes/blue-penguin-dark-master-en"

URL_PRE = 'en-'
INDEX_SAVE_AS = URL_PRE + 'index.html'
ARCHIVES_SAVE_AS = URL_PRE + 'archives.html'
AUTHORS_SAVE_AS = URL_PRE + 'authors.html'
CATEGORIES_SAVE_AS = URL_PRE + 'categories.html'
TAGS_SAVE_AS = URL_PRE + 'tags.html'
ARTICLE_URL = URL_PRE + "{slug}.html"
ARTICLE_SAVE_AS = URL_PRE + "{slug}.html"
PAGE_URL = URL_PRE + 'pages/{slug}'
PAGE_SAVE_AS = URL_PRE + 'pages/{slug}.html'
