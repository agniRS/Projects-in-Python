#!/bin/env python3
f='/home/a/test2.txt'
f=input()
fileloc=open(f,'r')
file=fileloc.read()
k=input("column no.:")
k=int(k)
file=file.split('\t')
j=len(file)
j=int(j)
c=k
c=int(c)
c=c-1
#totalnoofrows12
if k  == 0:
    print("error no 0th column")
elif k > 12:
    print("error k value exceeds file size")
else:
    while c <= j:
        print(file[c],"\t")
        c=c+11


