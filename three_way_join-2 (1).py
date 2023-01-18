#!/bin/env python3
chrinf=open('/home/a/knownGene(1).txt','r')
gninf=open('/home/a/kgXref.txt','r')
infds=open('/home/a/Downloads/InfectiousDisease-GeneSets.txt','r')
c=chrinf.read()
g=gninf.read()
dz=infds.read()
c=c.split()
g=g.split()
dz=dz.split()
lc=int(len(c))
lg=int(len(g))
ldz=int(len(dz))
gname=['Gene']
uscid=['ID']
chrm=['Chr']
start=['Start']
stop=['Stop']
for i in range(ldz):
    for j in range(4,lg,9):
        if dz[i] == g[j]:
            gname.append(g[j])
            uscid.append(g[j-4])
lid=int(len(uscid))
for k in range(lid):
    for m in range(lc):
        if uscid[k] == c[m]:
            chrm.append(c[m+1])
            start.append(c[m+3])
            stop.append(c[m+4])
#printing the output
z=0
print(gname,chrm,start,stop,uscid)
print(len(gname)," ",len(chrm)," ",len(start)," ",len(stop),"\n")
while z <lid:
    print(gname[z],'\t',chrm[z],'\t',start[z],'\t',stop[z])
    z=z+1


    

