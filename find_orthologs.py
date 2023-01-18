#!/bin/env python3
import os 
import sys
import multiprocessing
import subprocess
import argparse
parser = argparse.ArgumentParser()
i1=parser.add_argument('-i1', type=str, required=True)
i2=parser.add_argument('-i2', type=str, required=True)
o=parser.add_argument('-o', type=str, required=True)
t=parser.add_argument('-t', type=str, required=True)
ortho = parser.parse_args()
if1f=open(ortho.i1,'r')
if2f=open(ortho.i2,'r')
if ortho.t== 'p':
    tvalue="prot"
else:
    tvalue="nucl"
subprocess.call(["makeblastdb", "-in",ortho.i1,"-dbtype",tvalue])

subprocess.call(["makeblastdb", "-in",ortho.i2,"-dbtype",tvalue])

#database done
print("running blast.....")
if tvalue== "nucl":
    subprocess.call(["blastn","-query",ortho.i1,"-db",ortho.i2,"-out","of1","-outfmt","6","-max_hsps","1","-max_target_seqs","1"])
    subprocess.call(["blastn","-query",ortho.i2,"-db",ortho.i1,"-out","of2","-outfmt","6","-max_hsps","1","-max_target_seqs","1"])
else:
    subprocess.call(["blastp","-query",ortho.i1,"-db",ortho.i2,"-out","of1.txt"])
    subprocess.call(["blastp","-query",ortho.i2,"-db",ortho.i1,"-out","of2.txt"])

#comparing output files
coun3=0
#cleaning the files
subprocess.call(["cut","-f","1-2","of1"],stdout=open('of1+',"w"))
subprocess.call(["cut","-f","1-2","of2"],stdout=open('of2+',"w"))
#generated output files without only gene names
list1=[]
list2=[]
list3=[]
list4=[]
def rev_sentence(sentence):
 
    # first split the string into words
    words = sentence.split(' ')
    string=[]
    # then reverse the split string list and join using space
    for word in words:
        string.insert(0,word)
    reverse_sentence = ' '.join(string)
 
    # finally return the joined string
    return reverse_sentence
with open('of1+','r') as f:
    list1=f.readlines() 
with open('of2+','r') as f:
    list2=f.readlines()
#convert output file to lists

l1=int(len(list1))
l2=int(len(list2))
print(l1,l2)

for i in list1:
    r=rev_sentence(i)
    list4.append(r)
with open('revtest','w') as f:
    for item in list4:
        f.write(item)
print(list4,"\t",list2)
#list matching

for val1 in list4:
    for val2 in list2:
        if val1 == val2:
            coun3+=1
            list3.append(val1)
print(coun3)
#outputfile generation
with open(ortho.o,'w') as f:
    for item in list3:
        f.write(item)

with open('README','w') as f:
    l1=str(l1)
    l2=str(l2)
    coun3=str(coun3)
    string1=("on blasting"+ ortho.i1 +"with "+ortho.i2 +"we get "+l1+" hits")
    string2=("on blasting "+ortho.i2+" with "+ortho.i1+" we get "+l2+" hits")
    string3=("number of orthologus genes found:"+coun3)
    f.write(string1)
    f.write(string2)
    f.write(string3)



