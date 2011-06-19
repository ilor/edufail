import urllib, urllib2
import re
import time
import sys
import codecs
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

from edufail.grabber import get_all

try:
    from settings import LOGIN, PASSWORD
except ImportError:
    print "No settings, did you cp?"
    raise

print "Will login with %s:%s" % (LOGIN, '*' * len(PASSWORD))
print get_all(LOGIN, PASSWORD)


