import urllib, urllib2
import re
import time
from parser import *

LOGIN=""
PASSWORD=""

main_url = "https://edukacja.pwr.wroc.pl/EdukacjaWeb/studia.do"

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor)
urllib2.install_opener(opener)
main = urllib2.urlopen(main_url)

toks = re.findall('<input type="hidden".*?name="(.*?)".*?value="(.*?)">', main.read())

data = urllib.urlencode({"login":LOGIN, "password":PASSWORD[:20], toks[0][0]:toks[0][1], toks[1][0]:toks[1][1]})
log = urllib2.urlopen("https://edukacja.pwr.wroc.pl/EdukacjaWeb/logInUser.do", data=data)

index = urllib2.urlopen("https://edukacja.pwr.wroc.pl/EdukacjaWeb/indeks.do?clEduWebSESSIONTOKEN="+toks[0][1]+"&event=WyborSluchacza")


res_index = parse_index(index.read())
for sem, cours in res_index:
    for c in cours:
        print c[0], c[1], c[2], c[3], c[4]
        html_cours = urllib2.urlopen("https://edukacja.pwr.wroc.pl"+c[5])
        details = parse_course(html_cours.read())
	print details[0], details[1], details[2], details[3]
        time.sleep(5)
