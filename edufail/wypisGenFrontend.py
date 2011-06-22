# -*- coding: utf8 -*-
from grabber import get_all
from wypisGen import generate

import sys
import codecs
if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

import pickle #temp

from personalData import personalData, highSchoolName

#PRZYKLAD, TODO REMOVE

def readGrades(login, password):
    #dumpFile = open('grades.dmp')
    #grabberOutput = pickle.load(dumpFile)
    grabberOutput = get_all(login, password)
    grades = dict()
    average = 0;
    totalEcts = 0;
    totalHours = 0;
    for period, courses in grabberOutput.iteritems():
        (year, _, semester) = period.partition(' ')
        print "Got courses for: "+year
        for course in courses:
            if(course.grade == '2.0'):
                print "Skipping failed course..."
                continue

            if course.hours == '':
                course.hours = "0"
            if course.grade =='':
                course.grade = '0'
            totalHours += int(course.hours)
            average += float(course.grade) * int(course.ects)
            totalEcts += int(course.ects)
            hoursWeekly = str(int(course.hours)/15)
            courseDescription = [course.teacher,
                         course.name+" "+course.code]
            
            grading = [hoursWeekly if course.course_type == 'W' else '',            #liczba godzin wykladu
                       '' if course.course_type == 'W' else hoursWeekly,            #liczba godzin L/C
                       course.grade if course.form == 'Zaliczenie' else '',         #ocena przy zaliczeniu
                       course.grade_date if course.form == 'Zaliczenie' else '',    #data przy zaliczeniu
                       course.grade if course.form == 'Egzamin' else '',            #ocena przy egzaminie
                       course.grade_date if course.form == 'Egzamin' else '',       #data przy egzaminie
                       course.ects]                                                 #ects
            
            filler = ['', '', '', '', '', '', '']   #dla drugiego semestru

            if year not in grades:
                grades[year] = list()
            
            if(semester.lower() == "zimowy"):
                entry = courseDescription + grading + filler
                print "Winter course: " + str(entry)
                grades[year].insert(0, entry) #kurs zimowy idzie na przod listy kursow w roku

            else:
                entry = courseDescription + filler + grading
                print "Summer course: " + str(entry)
                grades[year].append(entry) #kurs letni idzie na koniec listy
    average = average / totalEcts
    return grades, average, totalHours


def generateAll(login, password):
    grades, average, hours = readGrades(login, password)
    #personalData and highschool name are temporarily globals filled above
    #TODO read from edu
    generate(personalData, highSchoolName, grades, str(round(average, 2)), str(max(3600, hours)))

