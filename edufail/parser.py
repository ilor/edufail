from lxml import etree
from itertools import izip
from StringIO import StringIO

def four_iter(iterable):
    it = iter(iterable)
    return izip(it, it, it, it)

def parse_index(index):

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(index), parser)

    cute_table = tree.findall("//table[@class='KOLOROWA']")[1]

    res = []
    for a, b, c, d in four_iter(cute_table.getchildren()):
        sem = a.getchildren()[2].text.strip()

        ret_cours = []
        courses = d.getchildren()[0].getchildren()[0].getchildren()
        for c in courses[1:]:
            link_node = c.getchildren()[0].getchildren()[0]
            code = link_node.text.strip()
            link = link_node.get("href")
            name =  c.getchildren()[1].text.strip()
            form = c.getchildren()[2].text.strip()
            ecst = c.getchildren()[3].text.strip()
            results = c.getchildren()[4].text.strip()
            ret_cours.append((code, name, form, ecst, results, link))
        res.append((sem, ret_cours))
    return res

def parse_course(html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(html), parser)

    cute_table = tree.findall("//table[@class='KOLOROWA']")[3]
    inner1 = cute_table.getchildren()[1].getchildren()[2].getchildren()[0]
    inner2 = cute_table.getchildren()[2].getchildren()[0].getchildren()[0]
    inner3 = cute_table.getchildren()[3].getchildren()[0].getchildren()[0]

    date = inner3.getchildren()[1].getchildren()[1].text.strip()
    who = inner1.getchildren()[1].getchildren()[1].text.strip()
    hours = inner2.getchildren()[2].getchildren()[3].text.strip()
    form = inner2.getchildren()[2].getchildren()[6].text.strip()

    return (who, hours, form, date)

