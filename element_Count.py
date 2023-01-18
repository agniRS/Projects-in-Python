#!/usr/bin/env python3
import argparse
import sys
import re
parser=argparse.ArgumentParser()
i1=parser.add_argument('-i',type=str,required=True)
elcount=parser.parse_args()
rows=[]
#checks for maximum count using first and last line
def maxcount(start,stop,rows):
    lastline=rows[(int(len(rows))-1)]
    firstline=rows[0]
    pos1=rows.index(start)
    st=int(stop)-1
    pos2=rows.index(st)
    for i in range(pos1,pos2):
        count=int(lastline[i])
        if maxc < count:
            maxc=count
    return maxc
#fills up the rows of the matrix with 0s and 1s,first fills up whole list of length max-min with 0s then just replaces the 0s with ones according tostart/stop         
def perlinecount(start,stop,maxm,minm):
    st=int(start)
    sp=int(stop)
    list1=[]
    for j in range((int(maxm)-int(minm))):
        list1.append('0')

    for i in range(st,(sp-1)):
        ind=list1.index(i)
        list1[ind]='1'
    return list1
#main fxns
#readfile
with open(elcount.i,'r') as f1:
    linewise=f1.readlines()
#this block of code is to mind max and min points of the matrix/max and min positions    
maxm=0
ko=linewise[1].split()
minm=int(ko[1])
for item in linewise:
    line=item.split()
    chrm=line[0]
    start=line[1]
    stop=line[2]
    big=int(stop)
    small=int(start)
    if maxm<big:
        maxm=big
    if minm>small:
        minm=small
#generation of matrix with positions as headers and the matrix is filled with 0s and 1s depending on query(chrm /start/stop)
temp=[]
for l in range(minm,(maxm-1)):
    temp.append(str(l))
''.join(temp)
rows.append(temp)
#filling up the matrix as list of lists[[list of column elements]...across no. of rows]
for itemx in linewise:
    linex=itemx.split()
    chrmx=line[0]
    startx=line[1]
    stopx=line[2]
    rows.append(perlinecount(startx,stopx,maxm,minm))
vals=0
csum=0
citems=[0]
#add total count of rows as a list at the end of the matrix file
for itemy in rows:
    for z in range(int(len(itemy))):
         citem=int(itemy[z])
         c=int(citems[z])
         csum=c+citem
         citems.append(csum)
rows.append(citems)

finalfl=[]
print(rows[0][0])   
#generating the output
for itemz in linewise:
    linez=itemz.split()
    chrmz=linex[0]
    startz=linex[1]
    stopz=linex[2]
    ec=maxcount(startz,stopz,rows)
    oline=f"{chrmz}\t{startz}\t{stopz}\t{ec}"
    finalfl.append(oline)
#making the file
flname=f"{elcount.i}.output"
with open(flname,'w') as f:
    for itema in finalfl:
        f.write(itema)

