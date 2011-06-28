#! /usr/bin/env python
import urllib, urllib2
import re
import time
import sys
import codecs
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

from edufail.grabber import get_all
from edufail.wypisGenFrontend import generateAll
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--add-score", type='int',
                  help="add ARG to ects*grade sum for average calc")
parser.add_option("--add-ects", type='int',
                  help="add ARG to ects sum for average calc")

(options, args) = parser.parse_args()


try:
    from settings import LOGIN, PASSWORD
except ImportError:
    print "No settings, did you cp?"
    raise

print "Will login with %s:%s" % (LOGIN, '*' * len(PASSWORD))

#print get_all(LOGIN, PASSWORD)
generateAll(LOGIN, PASSWORD, options)



