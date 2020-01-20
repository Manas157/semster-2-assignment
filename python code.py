# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:43:00 2020

@author: MANAS
"""

print(" answer should be either yes or no")
l=[]
l2=[]
x=input("i am a human being: ")
if x!='yes' and x!='no':
    print("given input is incorrect ")
    exit()
else:
    l.append(x)
y=input("i am good human being : ")
if y!='yes' and y!='no':
    print("given input is incorrect")
    exit()
else:
    l.append(y)
z=input("Good graders study well: ")
if z!='yes' and z!='no':
    print("given input is incorrect")
    exit()
else:
    l.append(z)
t=input("Humans love graders: ")
if t!='yes' and t!='no':
    print("given input is incorrect")
    exit()
else:
    l.append(t)
s=input("Every human does not study well: ")
if s!='yes' and s!='no':
    print("given input is incorrect")
    exit()
else:
    l.append(s)
print(l)
if l[0]=="yes" and l[1]=="yes" and l[2]=="yes" and l[3]=="yes" and l[4]=="no":
    print("every human is good grader")
else:
    print("No, every human is not a good grader")