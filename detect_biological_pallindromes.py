#!/usr/bin/env python3
str=input()
test=list(str)
l=len(test)
n=int(l/2)
comp=[]
for i in range(l):
    if test[i] == "A":
        comp.append("T")
    if test[i] == "T":
        comp.append("A")

    if test[i] == "G":
        comp.append("C")

    if test[i] == "C":
        comp.append("G")
print(test,comp) 
if l % 2 == 1:
    h1=test[:n]
    h2=test[:n:-1]
    ch1=comp[:n]
    ch2=comp[:n:-1]
else:
    h1=test[:n]
    h2=test[:n-1:-1]
    ch1=comp[:n]
    ch2=comp[:n-1:-1]
if h1 == ch2 and h2 == ch1:
    print("input string is a biological pallindrome")
else:
    print("input string is not a biological pallindrome")
        


