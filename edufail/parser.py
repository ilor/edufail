from lxml import etree
from itertools import izip
import itertools as it
from StringIO import StringIO

def four_iter(iterable):
    it = iter(iterable)
    return izip(it, it, it, it)

def parse_index(index):

    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(index), parser)

    tt = tree.xpath('//a[starts-with(@name, "hrefListaKursowTabela")]/parent::node()/parent::table')[0]

    sems = tt.xpath("child::node()[(position() + 3) mod 4 = 0]/td[2]/text()")
    res = []
    for sem, count in it.izip(sems, it.count(1)):
        sem = sem.strip()

        ret_cours = []
        courses = tt.xpath("child::node()[position() mod 4 = 0][$sem]/td/table/*[position() > 1]/td[position() > 1]/text()", sem=count)
        codes = tt.xpath("child::node()[position() mod 4 = 0][$sem]/td/table/*[position() > 1]/td[position() = 1]/a/text()", sem=count)
        urls = tt.xpath("child::node()[position() mod 4 = 0][$sem]/td/table/*[position() > 1]/td[position() = 1]/a/@href", sem=count)
        for (a, b, c, d), code, url in it.izip(four_iter(courses), codes, urls):
            name = a.strip()
            form = b.strip()
            ecst = c.strip()
            grade = d.strip()
            code = code.strip()

            ret_cours.append((code, name, form, ecst, grade, url))
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

