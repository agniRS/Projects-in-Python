#!/bin/env python3
fileloc=input("enter file location")
file=open(fileloc,'r')
seq=file.read()
k=input("enter k value")
k=int(k)
l=len(seq)
l=int(l)
kmer={}
for i in range(l-k+1):
    if seq[i:(i+k)] in kmer.keys():
        kmer[seq[i:(i+k)]]+=1
    else:
        kmer[seq[i:(i+k)]]=1
m=len(kmer)
m=int(m)

for j in kmer.keys():
    print(j,'\t',kmer[j],'\n')





