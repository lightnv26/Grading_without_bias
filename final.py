import json

#importing IBM Watson NaturalLanguageUnderstandingV1 api to get keywords for answers
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions

# importing tkinter for making python GUI
from tkinter import *
import csv

#taking data from original text file which is provided by teachers.
teacher = []
with open('.\data\original.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        row=" ".join(row)
        teacher.append(row)
#print(teacher)

#taking data from student_1 text file as answer sheet from students.
student_1 = []
with open('.\data\student_1.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        row=" ".join(row)
        student_1.append(row)
#print(student_1)

#taking data from student_2 text file as answer sheet from students.
student_2 = []
with open('.\data\student_2.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        row=" ".join(row)
        student_2.append(row)

#taking data from student_3 text file as answer sheet from students.
student_3 = []
with open('.\data\student_3.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        row=" ".join(row)
        student_3.append(row)

#taking data from student_4 text file as answer sheet from students.
student_4 = []
with open('.\data\student_4.txt', newline='') as inputfile:
    for row in csv.reader(inputfile):
        row=" ".join(row)
        student_4.append(row)

i=0
total_marks=0

#check function allot marks per question after it checks relevance data of common keywords in teacher and student file
def check(a,b):
    final_mark=0
    j=0 #for storing total number of matched keywords per answer

    #taking keywords from IBM Watson NaturalLanguageUnderstandingV1 api for student answersheet
    r1=printSomething(a)

    #taking keywords from IBM Watson NaturalLanguageUnderstandingV1 api for teacher answersheet
    r2=printSomething(b)

    #print(r1,r2)
    for key1,value1 in r2.items():
        for key,value in r1.items():
            #checking each keywords of teacher's answer is in student's answer or not.
            if key==key1:
                j=j+1
                diff=value1-value
                print('Keywords found :- ',key)
                print('\n')
                print('Value 1: ',value1," ,value 2: ",value)
                print('\n')

                if diff<0:
                    diff=diff*-1
                    print ("Difference between relevance value ",diff)
                    print('\n')
                else:
                    print(diff)
                    print('\n')
                #since maximum marks for a question is 1, therefore maximum alloted marks is 1 per question
                #alloting marks according to total numbers of keywords i.e., total marks = number of keywords.
                if diff>=0 and diff<=0.15:
                    final_mark=final_mark+1
                if diff>0.15 and diff<=0.35:
                    final_mark=final_mark+0.75
                if diff>0.35 and diff<=0.55:
                    final_mark=final_mark+0.5
                if diff>0.55 :
                    final_mark=final_mark+0.25


    print('Total words matched:- ',j)
    print('\n')
    if j==0:
        return 0
    return final_mark/j

#function returns keywords of given answers
def printSomething(t):
    res=[]
    rel=[]
    #using IBM api
    natural_language_understanding = NaturalLanguageUnderstandingV1(
      username='8b8545e7-9755-4efa-b65a-53fcbbe340ac',
      password='IakHD0SFzN5a',
      version='2017-02-27')


    response = natural_language_understanding.analyze(
      text=t,
      features=Features(
        keywords=KeywordsOptions(
          emotion=False,
          sentiment=False,
          limit=30)))


    for key in response['keywords']:
        res.append(key['text'])
        rel.append(key['relevance'])


    result = dict(zip(res, rel))
    return result
    #print(json.dumps(response, indent=2))


#for printing final marks of student 1 for this paper

for i in range(0,len(teacher)) :
    #print(i)
    #print(student_1[i],teacher[i])
    tot=check(student_1[i],teacher[i])
    print('Your marks for this question is ',tot)
    print('\n')
    total_marks=total_marks+tot

print('student 1 got ',total_marks,' out 0f 3')
print('\n')

#for student 2
total_marks2=0
for i in range(0,len(teacher)) :
    #print(i)
    #print(student_1[i],teacher[i])
    tot=check(student_2[i],teacher[i])
    print('Your marks for this question is ',tot)
    print('\n')
    total_marks2=total_marks2+tot


print('student 2 got ',total_marks2,' out 0f 3')
print('\n')

#for student 3
total_marks3=0
for i in range(0,len(teacher)) :
    #print(i)
    #print(student_1[i],teacher[i])
    tot=check(student_3[i],teacher[i])
    print('Your marks for this question is ',tot)
    print('\n')
    total_marks3=total_marks3+tot


print('student 3 got ',total_marks3,' out 0f 3')
print('\n')

#for student 4
total_marks4=0
for i in range(0,len(teacher)) :
    #print(i)
    #print(student_1[i],teacher[i])
    tot=check(student_4[i],teacher[i])
    print('Your marks for this question is ',tot)
    print('\n')
    total_marks4=total_marks4+tot


print('student 4 got ',total_marks4,' out 0f 3')
print('\n')


root = Tk()
root.title("Grade Sheets")
root.geometry('500x500')
Label(root, text="Student_1 Marks--").grid(row=0)
Label(root,text=total_marks).grid(row=0,column=8)
Label(root, text="Student_2 Marks--").grid(row=2)
Label(root,text=total_marks2).grid(row=2,column=8)
Label(root, text="Student_3 Marks--").grid(row=4)
Label(root,text=total_marks3).grid(row=4,column=8)
Label(root, text="Student_4 Marks--").grid(row=6)
Label(root,text=total_marks4).grid(row=6,column=8)


mainloop()
