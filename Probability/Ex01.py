import random
import itertools as it
from fractions import Fraction as f

def cau1a(sample_space):
    sum=0
    for event in sample_space:
        if event[0]==event[1]:
            sum+=1
    return f(sum,len(sample_space))
      
def cau1b(sample_space):
    sum=0
    for event in sample_space:
        if event[0]!=event[1]:
            sum+=1
    return f(sum,len(sample_space))

def cau1c(sample_space):
    sum=0
    for event in sample_space:
        if event[0]%2==0 and event[1]%2==0:
            sum+=1
    return f(sum,len(sample_space))

def cau1c(sample_space):
    sum=0
    for event in sample_space:
        if event[0]%2==0 and event[1]%2==0:
            sum+=1
    return f(sum,len(sample_space))

def cau1d(sample_space):
    sum=0
    for event in sample_space:
        if event[0]%2==1 and event[1]%2==1:
            sum+=1
    return f(sum,len(sample_space))

def cau1f(sample_space):
    sum=0
    for event in sample_space:
        if (event[0]%2==0 and event[1]%2==1) or (event[0]%2==1 and event[1]%2==0):
            sum+=1
    return f(sum,len(sample_space))

def cau1g(sample_space):
    sum=0
    for event in sample_space:
        if event[0]+event[1]>10:
            sum+=1
    return f(sum,len(sample_space))


dice2=[i+1 for i in range(6)]
dice1=[i+1 for i in range(6)]
sample_space=list(it.product(dice1,dice2))
print("a)",cau1a(sample_space))
print("b)",cau1b(sample_space))
print("c)",cau1c(sample_space))
print("d)", cau1d(sample_space))
print("f)", cau1f(sample_space))
print("g)", cau1g(sample_space))