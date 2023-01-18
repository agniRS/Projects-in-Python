#!/bin/env python3
#A  k-mer  is  a sequence of length k; for example, k-mers of length 2 (k=2) for DNA are AA, AT, AG, AC, CC, CT, CG, CA, TT, TA, TG, TC, GG, GC, GT, and GA
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





