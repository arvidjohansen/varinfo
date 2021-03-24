"""
varinfo is a library of helper-functions
designed to make your life easier when 
exploring new packages, modules, classes and objects.
"""

from .functions import varinfo, udir, grep
from .displayhook import pprint

__all__ = ['udir','varinfo','pprint','grep']


