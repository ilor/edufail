# -*- coding: utf8 -*-
import codecs
import subprocess

def assembleGrades(gradesInYear):
    print gradesInYear
    line = unicode("")
    for course in gradesInYear:
        print "Assembling course: "+unicode(course)
        line += u"\hline "
        line += u" & ".join(course)
        line += u" \\\ \n"
        #print unicode('\tAssembled as: ') + line
    return line

def generateInYear(personalData, gradesInYear, extraReplace, outFileName):
    f = codecs.open("template.tex", 'r', 'utf8')
    content = unicode(f.read())

    #personal data fill
    for k, v in personalData.iteritems():
        #print u"Personal data, replacing: "+unicode(k, errors='replace')+u" with: "+unicode(v, errors='replace')
        content = content.replace(k, v)
    content = content.replace("%@grades@", assembleGrades(gradesInYear))
    for k, v in extraReplace.iteritems():
        content = content.replace(k, v)
    
    out = codecs.open(outFileName, 'w', 'utf8')
    out.write(content)
    out.close()
    print "Attempting to compile "+outFileName+" with pdflatex..."
    subprocess.call(['pdflatex',outFileName])
    print "Second run..."
    subprocess.call(['pdflatex',outFileName])
    

def generate(personalData, highSchool, grades, averageGrade, totalHours):
    years = sorted(grades)
    print years
    lastSchool = highSchool
    for i in range(0, len(years)):
        year = years[i]
        extraReplace = dict()
        extraReplace["%@academicYear@"] = year
        extraReplace["%@lastSchool@"] = lastSchool
        if i == len(years)-1:
            #last year, add average and total hours
            extraReplace['%@avgAndSum@'] = "Średnia ocen w toku studiów: ".decode("utf8")+averageGrade+"\n\nSuma godzin: "+totalHours
        generateInYear(personalData,
                       grades[year],
                       extraReplace,
                       'generated'+str(i)+".tex")
        lastSchool = "Politechnika Wrocławska".decode("utf8")
