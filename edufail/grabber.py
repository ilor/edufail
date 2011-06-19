import urllib, urllib2
import re
import time
from parser import *


_main_url = "https://edukacja.pwr.wroc.pl"

class CourseEntry:
    def __init__(self, code, name, course_type, grade, ecst, teacher, hours, form, grade_date):
        self.code = code
        self.name = name
        self.course_type = course_type
        self.grade = grade
        self.ecst = ecst
        self.teacher = teacher
        self.hours = hours
        self.form = form
        self.grade_date = grade_date

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.course_type, self.grade)

    def __str__(self):
        return unicode(self).encode("utf8")

    def __repr__(self):
        return "<" + str(self) + ">"

def get_all(login, password):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)
    urllib2.install_opener(opener)
    main = urllib2.urlopen(_main_url + "/EdukacjaWeb/studia.do")

    toks = re.findall('<input type="hidden".*?name="(.*?)".*?value="(.*?)">', main.read())
    data = urllib.urlencode({"login" : login, "password": password[:20], toks[0][0]:toks[0][1], toks[1][0]:toks[1][1]})
    log = urllib2.urlopen(_main_url + "/EdukacjaWeb/logInUser.do", data=data)

    index = urllib2.urlopen(_main_url + "/EdukacjaWeb/indeks.do?clEduWebSESSIONTOKEN=" + toks[0][1] + "&event=WyborSluchacza")

    parsed_index = parse_index(index.read())
    to_return = []
    for sem, cours in parsed_index:
    	course_infos = []
        for c in cours:
            html_cours = urllib2.urlopen(_main_url + c[5])
            course_details = parse_course(html_cours.read())

            entry = CourseEntry(c[0], c[1], c[2], c[4], c[3], course_details[0], course_details[1], course_details[2], course_details[3])
            course_infos.append(entry)
            time.sleep(1)
        to_return.append((sem, course_infos))
    return to_return
