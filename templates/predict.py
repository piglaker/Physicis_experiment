# -*- coding: utf-8 -*-
"""
Created on Tue May 28 01:30:41 2019

@author: msq
"""
import numpy as np
import torch
import struct
from torch import optim
import cv2

n_classes=10


class modeling(torch.nn.Module):
    def __init__(self,output_dim):
        super(modeling,self).__init__()
        
        self.conv=torch.nn.Sequential()
        self.conv.add_module("conv1",torch.nn.Conv2d(1,18,kernel_size=3,stride=2, padding=2)) 
        self.conv.add_module("dropout_1",torch.nn.Dropout(0.2))  
        self.conv.add_module("relu_1",torch.nn.ReLU()) 
        self.conv.add_module("conv2",torch.nn.Conv2d(18,32,kernel_size=3,stride=2, padding=2)) 
        self.conv.add_module("dropout_2",torch.nn.Dropout(0.2)) 
        self.conv.add_module("relu_2",torch.nn.ReLU())
        
        self.fc=torch.nn.Sequential()
        self.fc.add_module("fc_1",torch.nn.Linear(32*9*9,50))
        self.fc.add_module("relu_3",torch.nn.ReLU())
        self.fc.add_module("dropout_3",torch.nn.Dropout(0.2))
        self.fc.add_module("fc_2",torch.nn.Linear(50,output_dim))
        
    def forward(self,x):
        x=self.conv.forward(x)
        x=x.view(-1,32*9*9)
        return self.fc.forward(x)



def predict(model,x_val):
    x=torch.autograd.Variable(x_val.cuda(),requires_grad=False)
    output=model.forward(x)
    return output.cpu().data.numpy().argmax(axis=1)



def findBorderContours(img, maxArea=10):
    _, contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    borders = []
    
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w*h > maxArea:
            border = [(x, y), (x+w, y+h)]
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            borders.append(border)
    return borders,img



def transMNIST(img, borders, size=(28, 28)):
    imgData = np.zeros((len(borders), size[0], size[0], 1), dtype='uint8')
    for i, border in enumerate(borders):
        borderImg = img[border[0][1]:border[1][1], border[0][0]:border[1][0]]
        extendPiexl = (max(borderImg.shape) - min(borderImg.shape)) // 2
        targetImg = cv2.copyMakeBorder(borderImg, 7, 7, extendPiexl + 7, extendPiexl + 7, cv2.BORDER_CONSTANT)
        targetImg = cv2.resize(targetImg, size)
        targetImg = np.expand_dims(targetImg, axis=-1)
        imgData[i] = targetImg
    return imgData



def new_borders(borders,i):
    if borders[i][1][1]>borders[i+1][1][1]:
        ymax=borders[i][1][1]
    else:
        ymax=borders[i+1][0][1]
    if borders[i][0][1]>borders[i+1][0][1]:
        ymin=borders[i+1][0][1]
    else:
        ymin=borders[i][0][1]
    xmin,xmax=borders[i][0][0],borders[i+1][1][0]
    del(borders[i+1])
    borders[i][0],borders[i][1]=(xmin,ymin),(xmax,ymax)
    return borders

    
    
    
   
def rearrange(borders): 
    for i in range(len(borders)):
        for j in range(i+1,len(borders)):
            if borders[i][0][0]>borders[j][0][0]:
                borders[i],borders[j]=borders[j],borders[i]
    return borders



    
    

if __name__ == '__main__':
    path = 'C://Users//Acer//Desktop//q.jpg'
    test=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    test=np.array(test)
    test=255-test
    blur = cv2.GaussianBlur(test,(5,5),0)
    ret3,test = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    borders,rect = findBorderContours(test)
    borders=rearrange(borders)
    
    i=0
    while True:
        x_right,y_right,x_left,y_left=borders[i][1][0],borders[i][1][1],borders[i+1][0][0],borders[i+1][0][1]
        if x_right>x_left and y_right>y_left:
            borders=new_borders(borders,i)
        i+=1
        if (i+2)==len(borders):
            break
            
    tests = transMNIST(test, borders)
   
    
    for i in range(tests.shape[0]):
        img=tests[i,:,:,0]
        name = 'C://Users//Acer//Desktop//extract//test_' + str(i) + '.jpg'
        cv2.imwrite(name, img)
        
        
    model=modeling(output_dim=n_classes)
    model=torch.load("./model/models_900.pth")
    tests=np.array(tests)
    test=torch.from_numpy(tests).float()
    test = test.reshape(-1, 1, 28, 28)
    predY=predict(model,tests)
    print(predY)
    



