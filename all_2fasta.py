#!/usr/bin/env python3
import argparse
import sys
import re
parser=argparse.ArgumentParser()
i=parser.add_argument('-i',type=str,required=True)
fold=parser.add_argument('-f',type=str,required=True)
fasta=parser.parse_args()

#checking fxn #checks filetype and returns it
def flcheck(linewise):
    firstline=str(linewise[0]).split()
    firstword=firstline[0]
    firstchar=(str(firstword[0]))

    if firstword=="ID":
        typ="EMBL"
    elif firstword=="LOCUS":
        typ="GB"
    elif firstword=="#mega":
        typ="MEGA"
    elif firstword=="@HD" or "@SQ" or "@RG" or "@PG":
        typ="SAM"
    elif firstchar[0]=="@":
        typ="FASTQ"
    elif firstchar[:1]=="##":
        typ="VCF"
    return typ

 #defining each fxn
 #each fxn also checks aa or nu (adds format type to beginning of list) and divides bases accrding to fold
 #fastq
def fastq(fold,linewise):
    fastq=[]
    for z in  range(int(len(linewise))):
        if linewise[i] == "+":
            line=str(linewise[z-2])
            identifier=line[1:]
            seq=str(linewise[z-1])
            seq1=seq.split()
            f=int(fold)
            for h in range(f,int(len(seq1)),f):
                seq1.insert(h,'\n')
            for item in seq1:
                if item == 'A'or 'T' or 'G' or 'C' or 'N':
                    frmt='.fna'
                if item != 'A'or 'T' or 'G' or 'C' or 'N':
                    frmt='.faa'
                    break
        seq=''.join(seq1)           
        fl=f'>{identifier}\n{seq}\n'
        fastq.append(fl)
    fastq.insert(0,frmt)
    return fastq

  #vcf 
def vcf(fold,linewise):
    vcf=[]
    ref=[]
    sample=[]
    seq=[]
    for i in range(int(len(linewise))):
        line=str(linewise[i]).split()
        if line[0]=='#CHROM':
            lineX=str(linewise[i+1]).split()
            refname=lineX[0]
            sampleno=int(len(lineX))-9
            ref.append(lineX[3])
#alt checking
            alt=str(lineX[4]).split(',')
#making samples
            for j in range(sampleno):
                nex=str(lineX[j])
                nex=int(nex[0])
                nexbase=str(alt[nex])
                prevbase=seq[j]
                seqc=prevbase+nexbase
                lseq=int(len(seqc))
                if lseq==int(fold):
                    seqc=seqc+'\n'
                seq[j]=seqc
    ref=''.join(ref)
    firstline=f">{refname}\n{ref}"
    vcf.append[firstline]
    for k in range(sampleno):
        sample=f">sample{k+1}\n{seq[k]}\n"
        vcf.append(sample)
        for item in seq[k]:
                        if item == 'A'or 'T' or 'G' or 'C' or 'N':
                            frmt='.fna'
                        if item != 'A'or 'T' or 'G' or 'C' or 'N':
                            frmt='.faa'
                            break
    vcf.insert(0,frmt)
    return sample
  #sam
def sam(fold,linewise):
    sam=[]
    for i in range(int(len(linewise))):
        line=str(linewise[i]).split()
        if int(len(line)) >=11:
            identifier=line[0]
            seq=line[9]
            seq1=seq.split()
            f=int(fold)
            for h in range(f,int(len(seq1)),f):
                seq1.insert(h,'\n')
            for item in seq1:
                            if item == 'A'or 'T' or 'G' or 'C' or 'N':
                                frmt='.fna'
                            if item != 'A'or 'T' or 'G' or 'C' or 'N':
                                frmt='.faa'
                                break
            seq=''.join(seq1)
            fl=f">{identifier}\n{seq}\n"
            sam.append(fl)
    sam.insert(0,frmt)
    return sam
        

  #mega
def mega(fold,linewise):
    mega=[]
    for i in  range(int(len(linewise))):
        if linewise[i] == "#MEGA":
            line=str(linewise[i+3])
            identifier=line[1:]
            seq=str(linewise[i+4])
            seq1=seq.split()
            f=int(fold)
            for h in range(f,int(len(seq1)),f):
                seq1.insert(h,'\n')
            for item in seq1:
                if item == 'A'or 'T' or 'G' or 'C' or 'N':
                    frmt='.fna'
                if item != 'A'or 'T' or 'G' or 'C' or 'N':
                    frmt='.faa'
                    break
            seq=''.join(seq1)
            fl=f">{identifier}\n{seq}\n"
            mega.append(fl)

    mega.insert(0,frmt)
    return mega
  #genebank
def gb(fold,linewise):
    gb=[]
    seq=[]
    frmt=''
    for i in  range(int(len(linewise))-1):
        line=str(linewise[i]).split()
        if linewise[i] == "ORIGIN":
            line1=str(linewise[i+1]).split()
            for item in line1:
                if item.isnumeric()==False:
                    capseq=item.upper()
                    seq.append(capseq)
            f=int(fold)
            for h in range(f,int(len(seq)),f):
                seq.insert(h,'\n')
            for item in seq:
                        if item == 'A'or 'T' or 'G' or 'C' or 'N':
                            frmt='.fna'
                        if item != 'A'or 'T' or 'G' or 'C' or 'N':
                            frmt='.faa'
                            break       
            seq=''.join(seq)

        if str(line[0]) == "VERSION":
            identifier=line[1]
    fl=f">{identifier}\n{seq}\n"
    gb.append(fl)
    gb.insert(0,frmt) 
    return gb

  #embl
def embl(fold,linewise):
    embl=[]
    seq=''
    for i in  range(int(len(linewise))):
        line=str(linewise[i]).split()
        if line[0]=='ID':
            temp=str(line[1])
            ln=int(len(temp))
            idn=temp[:ln-1]
            sv=line[3]
            identifier=f"{idn}.{sv}"
        if line[0]=='DE':
            descr=''.join(line)
            descr=descr[1:]
        if line[0]=='SQ':
            for j in range(i+1,int(len(linewise)),2):
                lineY=linewise[j].split()
                miniseq=''.join(lineY)
                miniseq=miniseq.upper()
                seq=seq+miniseq
            seq1=seq.split()    
            f=int(fold)
            for h in range(f,int(len(seq1)),f):
                seq1.insert(h,'\n')
            for item in seq1:
                if item == 'A'or 'T' or 'G' or 'C' or 'N':
                    frmt='.fna'
                if item != 'A'or 'T' or 'G' or 'C' or 'N':
                    frmt='.faa'
                    break
            seq=''.join(seq1)
        fl=f">ENA|{idn}|{identifier} {descr}\n{seq}"
        embl.append(fl)    
    embl.insert(0,frmt)
    return embl
with open(fasta.i,'r') as f:
    ls1=f.readlines()
with open(fasta.i,'r') as f1:
    linewise=f1.readlines()
typ= flcheck(linewise)
    
#conversion
if typ=="EMBL":
     list2=embl(fold,linewise)
if  typ=="GB":
    list2=gb(fold,linewise)
elif typ=="MEGA":
    list2=mega(fold,linewise)
elif typ=="SAM":
    list2=sam(fold,linewise)
elif typ=="VCF":
    list2=vcf(fold,linewise)
elif typ=="FASTQ":
    list2=fastq(fold,linewise)

#writing the file with the format (frmt deleted from list of elements)
frmt=str(list2[0])
flname=f"{fasta.i}.{frmt}"
del list2[0]
with open(flname,'w') as f:
    for item in list2:
        f.write(item)
