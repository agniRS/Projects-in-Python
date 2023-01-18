#!/usr/bin/python env3
import argparse
import sys
import re
import os
parser=argparse.ArgumentParser()      #argparse arguments
i1=parser.add_argument('-i1',type=str,required=True)
i2=parser.add_argument('-i2',type=str,required=True)
m=parser.add_argument('-m',type=int,required=True)
parser.add_argument('-j',action="store_true")
o=parser.add_argument('-o',type=str,required=True)
oB=parser.parse_args()
#overlap fxn
def overlap(start1,stop1,start2,stop2):
    start1=int(start1)
    stop1=int(stop1)
    start2=int(start2)
    stop2=int(stop2)
    o=min(stop1,stop2)-max(start1,start2)
    if o <=0:
        overlap=0
    else:
        overlap=(o/(stop1-start1))*100
    return overlap
#main fxn
list1=[]
count=0
list2=[]
with open(oB.i2,'r') as f:             #read both files
    linewisef2=f.readlines()
with open(oB.i1,'r') as f1:
    linewisef1=f1.readlines()
list4=[]
str2='\n'.join(linewisef2)
list3=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']
for i in list3:
    z=re.findall(rf"{i}.*",str2)  # create list of lists with each nested list corresponding to particular chromosome for file 2 eg:[['chr1 200 300','chr1...'..],['chr2 200 300'...]...]
    list2.append(z)
    list2.append(z)
str3='\n'.join(linewisef1)
for j in list3:
    x=re.findall(rf"{j}.*",str3) # create list of lists with each nested list corresponding to particular chromosome for file 1 eg:[['chr1 200 300','chr1...'..],['chr2 200 300'...]...]
    list2.append(z)
    list4.append(x)
index=0
print("lists created")
for item in list4:
    chromosome=list2[index]  #select chr list in fl2 list
    cnt=0
    for minitem in item:
        vals1=item[cnt].split('\t') #get chr associated list of lines from f1
        for item1 in chromosome:
            vals2=chromosome[cnt].split('\t')  #get chr associated list of lines from f2
            if vals1[2]<vals2[1]:
                break            #constraint to lessen number of checks
            olp=overlap((vals1[1]),(vals1[2]),vals2[1],vals2[2])
            if olp >= oB.m:
                if oB.j:
                    str1=item[cnt]+'\t'+item1       # cnt is also a constraint to lessen number of checks
                    list1.append(str1)
                    count+=1
                else:
                    list1.append(item[cnt])
                    count+=1
        cnt+=1
    index+=1
#remove dupliates
list5=list(dict.fromkeys(list1))
with open(oB.o,'w') as wt:             #write output file
    for item2 in list5:
        wt.write(item2)
with open('README','w') as wt:
    str2=f"Number of lines is {count}"  #write README file
    wt.write(str2)