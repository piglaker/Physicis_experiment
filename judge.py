import numpy as np

score=np.loadtxt(r'./score.txt',dtype=int)
error=np.zeros((1,5),dtype=int)
if score[1]==0:
    error[0][0]=1
if score[2]<2:
    error[0][1]=1
if score[3]<2:
    error[0][2]=1
if score[4]<1:
    error[0][3]=1
print(error)