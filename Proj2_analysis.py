#Ben Moreau

import numpy as np
from math import *
from matplotlib import pyplot as plt
import os

Num_exp=np.genfromtxt("param.txt",skip_header=1)[101,0]
Num_rolls=np.genfromtxt("param.txt",skip_header=1)[101,1]
Num_sides=np.genfromtxt("param.txt",skip_header=1)[101,2]
Side_number=np.genfromtxt("param.txt",skip_header=1)[101,3]
DPL=np.genfromtxt("param.txt",skip_header=1)[101,4]
DPU=np.genfromtxt("param.txt",skip_header=1)[101,5]
LogLikeRatio0I=np.genfromtxt("log_like0.txt",skip_header=0)[:,0]
LogLikeRatio1I=np.genfromtxt("log_like1.txt",skip_header=0)[:,0]
#print("A")
LogLikeRatio0=[]
LogLikeRatio1=[]
for i in range(len(LogLikeRatio0I)):
    LogLikeRatio0.append((LogLikeRatio0I[i]))
    LogLikeRatio1.append((LogLikeRatio1I[i]))

Num_rolls=int(Num_rolls)
# make LLR figure

plt.hist(LogLikeRatio1, Num_rolls+1, density=True, facecolor='green', alpha=0.7, label="assuming $\\mathbb{H}_1$")
plt.hist(LogLikeRatio0, Num_rolls+1, density=True, facecolor='red', alpha=0.7, label="assuming $\\mathbb{H}_0$")

print("Number of experiments:")
print(Num_exp)
print("Number of rolls per experiment:")
print(Num_rolls)
print("Number of sides on the die:")
print(Num_sides)
print("Test side number:")
print(Side_number)
print("Lower limit for the exponential die weight:")
print(DPL)
print("Upper limit for the exponential die weight:")
print(DPU)
#print("A")
#
#
#
#Create an array containing sorted probability values
#
#
#

LogLikeRatio1=sorted(LogLikeRatio1)#use built in sorted
LogLikeRatio0=sorted(LogLikeRatio0)
#print("A")
#Full_L=[]

#print(LogLikeRatio0)
#print(LogLikeRatio1)
#print(Both_L)


for i in range(len(LogLikeRatio0)):
    '''
    if(int(LogLikeRatio0[i])==int(LogLikeRatio1[i])):
        #print("Y")
        L=0
        L1=0
        for a in range(len(LogLikeRatio0)):
            if(int(LogLikeRatio0[i])==int(LogLikeRatio0[a])):
                L+=1
            if(int(LogLikeRatio1[i])==int(LogLikeRatio1[a])):
                L1+=1
        if(L1>L):
            Full_L.append(LogLikeRatio0[i])
            
        elif (L>L1):
            Full_L.append(LogLikeRatio1[i])
            
        else:
            Full_L.append(LogLikeRatio1[i])
            #print("B")#Find the amount of times the values occur, taking the lower amount if they occur in both functions
    else:
        Full_L.append(LogLikeRatio0[i])
        Full_L.append(LogLikeRatio1[i])
        #print("A")

    '''







#
#
#
#Find lambda_alpha and beta
#
#
#
alpha=0.1






Lambda_alpha=LogLikeRatio0[int(len(LogLikeRatio0)*(1-alpha))]

Beta=0
for i in range(len(LogLikeRatio1)):
    if(LogLikeRatio1[i]>Lambda_alpha):
        Beta=i/len(LogLikeRatio0)#To find beta, I look for the portion of values that fall below $\lambda_\alpha$ in the sorted LLR1 array, and that is the probability of falsely rejecting the H1 theory.
        break;
print("For an alpha value of ",alpha,"Lambda alpha is",Lambda_alpha,"And beta is",Beta)
plt.hist([Lambda_alpha,Lambda_alpha+1,Lambda_alpha-1],1,label="$\\lambda_\\alpha$",color="black")
#print("A")    
#Full_L=sorted(Full_L)

#print(Full_L)
#plt.hist(Full_L,Num_rolls+1,facecolor="orange",alpha=.5,density=True)
mn=0
mx=0
if(min(LogLikeRatio0)<min(LogLikeRatio1)):
    mn=min(LogLikeRatio0)
else:
    mn=min(LogLikeRatio1)
if(max(LogLikeRatio0)<max(LogLikeRatio1)):
    mx=max(LogLikeRatio1)
else:
    mx=max(LogLikeRatio0)
    
   
plt.legend()
plt.xlim(mn,mx )
plt.ylim(0,1)

plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
plt.ylabel('Probability')
plt.title("H_0 is a fair dice cube, H_1 has a weight with random distribution from "+str(DPL)+" to "+str(DPU))
plt.grid(True)
plt.show()



print("A")

'''
a= plt
a.hist(Exp_successes,Num_rolls)
a.title("Number of successful rolls in an experiment")
a.show()
b=plt
b.hist(Exp_res,Num_rolls)
b.title("Probability of success in an experiment")
b.show()
'''













