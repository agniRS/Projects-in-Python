#!/usr/bin/env python3
num=input()
n=int(num)
a=0
b=1
fibonacci=[]
for i in range(n):
    fibonacci.append(a)
    temp=a
    a=a+b
    b=temp
print(fibonacci)
    

