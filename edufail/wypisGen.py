# -*- coding: utf8 -*-

def assembleGrades(gradesInYear):
    print gradesInYear
    line = ""
    for course in gradesInYear:
        line += "\hline "
        line += ( " & ".join(course))
        line += (" \\\ \n")
    return line

def generateInYear(personalData, lastSchool, academicYear, gradesInYear, outFileName):
    f = open("template.tex")
    content = f.read()

    #personal data fill
    for k, v in personalData.iteritems():
        content = content.replace(k, v)

    content = content.replace("%@academicYear@", academicYear)
    content = content.replace("%@lastSchool@", lastSchool)

    content = content.replace("%@grades@", assembleGrades(gradesInYear))
    out = open(outFileName, 'w')
    out.write(content)

def generate(personalData, highSchool, grades):
    years = sorted(grades)
    print years
    generateInYear(personalData, highSchool, years[0], grades[years[0]], 'generated0.tex')

    for i in range(1, len(years)):
        year = years[i]
        generateInYear(personalData, "Politechnika Wrocławska", year, grades[year], 'generated'+str(i)+".tex")


#PRZYKLAD, TODO REMOVE
personalData = {
    '%@indexNumber@' : "157636",
    '%@name@' : "Maciej",
    '%@lastName@' : "Pawłowski",
    '%@birth@' : "1987-09-07 Zielona Góra",
    '%@localAddress@' : "adres bleble",
    '%@parents@' : "Jacek, Wiesława, Wynagrodzenie z tytułu umowy o pracę",
    '%@parentsAddres@' : "adres blabla",
    '%@milRank@' : "",
    '%@milSpec@' : "",
    '%@milEvid@' : "wtf",
    '%@wkr@' : "Zielona Góra",
    '%@phone@' : ""
    }

wpis1 = ["prof dr hab inz med kowalski", "matma INZ007W", '2', '', '3.5', '12-12-2006', '', '', '4', '', '', '', '', '', '', ''] #sem zimowy
wpis2 = ["dr hab inż nowak", "matma C INZ007C", '', '3', '4.5', '28-12-2006', '', '', '3', '', '', '', '', '', '', ''] #sem zimowy
wpis3 = ["starszy przedwieczny cthulu", "gorsza matma W INZ66601W", '4', '', '', '', '', '', '', '4', '', '', '', '5.0', '01-01-2007', '6'] #sem letni
wpis4 = ["master chief", "bd", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'] #juz mi sie nie chcialo
wpis5 = ["szatan", "penis", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

grades = {
    '2006/2007' : [wpis1, wpis2, wpis3],
    '2007/2008' : [wpis4, wpis5]
    }

generate(personalData, "Moje liceum", grades)
