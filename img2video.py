# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:50:00 2019

@author: Acer
"""
import numpy as np
import cv2

def add_frame_all(sx1,sy1,sx2,sy2,num,img_root):
    for i in range(num):
        
        im=cv2.imread(img_root+str(i+1)+".jpg")
        cv2.rectangle(im,(int(sx1),int(sy1)),(int(sx2),int(sy2)),(0,255,0),3)
        cv2.imwrite(img_root+str(i+1)+".jpg",im)

def add_frame_part(sx1,sy1,sx2,sy2,num,change_num,img_root):
    for i in range(change_num):
        im=cv2.imread(img_root+str(num-change_num+i)+".jpg")
        cv2.rectangle(im,(int(sx1),int(sy1)),(int(sx2),int(sy2)),(0,0,255),3)
        cv2.imwrite(img_root+str(num-change_num+i)+".jpg",im)

def trans2video_sound(temp,img_root):
    
    fps = 20    #保存视频的FPS，可以适当调整
    size=(640,480)
    #可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter('./static/img/video2.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸

    for i in range(50):
        frame = cv2.imread(img_root+str(temp-25+i)+'.jpg')
        videoWriter.write(frame)
    videoWriter.release()

def trans2video_font(path,num):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps=20
    size=(640,480)

    videoWriter = cv2.VideoWriter('./static/img/video4.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸
    for i in range(2):
        frame = cv2.imread(path+str(num-2+i)+".jpg")
        videoWriter.write(frame)
    videoWriter.release()

    
def trans2video_end(img_root,num):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps=20
    size=(640,480)
    videoWriter = cv2.VideoWriter('./static/img/video3.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸
    for i in range(2):    
        frame = cv2.imread(img_root+str(num-2+i)+".jpg")
        videoWriter.write(frame)
    videoWriter.release()


def move2target(target,num):
    im = cv2.imread("./img/"+str(target)+".jpg")
    cv2.imwrite("./pytorch-ssd-master/images_folder/1.jpg",im)
    for j in range(2):
        im = cv2.imread("./img/"+str(num-2+j)+".jpg")
        cv2.imwrite("./pytorch-ssd-master/images_folder/" + str(j + 2) + ".jpg", im)
    for k in range(50):
        im = cv2.imread("./img/" + str(target - 2*k ) + ".jpg")
        cv2.imwrite("./pytorch-ssd-master/images_folder/" + str(k + 4) + ".jpg", im)


def trans2video_all(img_root,num):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps=20
    size=(640,480)
    videoWriter = cv2.VideoWriter('./static/img/video1.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸
    for i in range(num):    
        frame = cv2.imread(img_root+str(i)+".jpg")
        videoWriter.write(frame)
    videoWriter.release()
    

def add_font(path):
    im=cv2.imread(path)
    cv2.putText(im, "true answer is : 1.60", (int(30),int(80)), cv2.FONT_HERSHEY_COMPLEX_SMALL,2, (0, 0,255) )
    cv2.imwrite(path,im)


if __name__ == '__main__':
    c = np.loadtxt(r'./destine.txt')
    temp = int(c[0])
    num = int(c[1])
    # 打点计时器部分
    #add_frame_all(90,370,130,400, num, "./img2/")
    #trans2video_all("./img2/", num)
    #trans2video_sound(temp, "./img2/")

    # 结尾部分
    #add_frame_part(120, 255, 260, 370, num, 2, "./img/")
    #trans2video_end("./img/", num)
    # 数字部分

    add_font("./img3/" + str(num - 2) + ".jpg")
    add_font("./img3/" + str(num - 1) + ".jpg")
    trans2video_font("./img3/", num)
    location=np.loadtxt("./location.txt",dtype=int)
    np.savetxt("./output_distance.txt.txt",[0])
    np.savetxt("./output_range_judge_path.txt",[location[0], location[1], location[2], location[3]])
    move2target(temp,num)