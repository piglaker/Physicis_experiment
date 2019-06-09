import cv2
import numpy as np

def trans2video_all(img_root,num):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps=20
    size=(640,480)
    videoWriter = cv2.VideoWriter('./static/img/video1.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸
    for i in range(num):
        frame = cv2.imread(img_root+str(i)+".jpg")
        videoWriter.write(frame)
    videoWriter.release()

def trans2video_end(img_root):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps=20
    size=(640,480)
    videoWriter = cv2.VideoWriter('./static/img/video3.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸
    for i in range(2):
        frame = cv2.imread(img_root + str(i+2) + ".jpg")
        videoWriter.write(frame)
    videoWriter.release()


def add_frame_part(sx1,sy1,sx2,sy2,img_root):
    for i in range(2):
        im=cv2.imread(img_root + str(i+2) + ".jpg")
        print(sx1,sy1,sx2,sy2)
        cv2.rectangle(im,(int(sx1),int(sy1)),(int(sx2),int(sy2)),(0,0,255),3)
        #cv2.rectangle(im, (int(0), int(0)), (int(320), int(240)), (0, 0, 255), 3)
        cv2.imwrite(img_root + str(i+2) + ".jpg",im)


def add_frame_all(sx1, sy1, sx2, sy2, num, img_root):
    for i in range(num):
        im = cv2.imread(img_root + str(i + 1) + ".jpg")
        cv2.rectangle(im, (int(sx1), int(sy1)), (int(sx2), int(sy2)), (0, 255, 0), 3)
        cv2.imwrite(img_root + str(i + 1) + ".jpg", im)


def trans2video_sound(temp, img_root):
    fps = 20  # 保存视频的FPS，可以适当调整
    size = (640, 480)
    # 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter('./static/img/video2.mp4', fourcc, fps, size)  # 最后一个是保存图片的尺寸

    for i in range(50):
        frame = cv2.imread(img_root + str(temp - 25 + i) + '.jpg')
        videoWriter.write(frame)
    videoWriter.release()


def add_frame_sound(sx1 ,sy1 ,sx2 ,sy2 ,target ,img_root):
    for i in range(50):
        im =cv2.imread(img_root +str( target - 25 + i  ) +".jpg")
        cv2.rectangle(im ,(int(sx1) ,int(sy1)) ,(int(sx2) ,int(sy2)) ,(0 ,255 ,0) ,3)
        cv2.imwrite(img_root +str( i - 25 + target ) +".jpg" ,im)


def move2target(target):
    for i in range(50):
        im = cv2.imread("./pytorch-ssd-master/ssd_output_img/"+str(i+1)+".jpg")
        cv2.imwrite("./img/"+str(target+i-25)+".jpg",im)



def move2loca(num):
    for i in range(2):
        im = cv2.imread("./pytorch-ssd-master/ssd_output_img/"+str(num + i -2)+".jpg")
        cv2.imwrite("./img/"+str(num + i - 2)+".jpg",im)

def trans2video_all(img_root, num):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 20
    size = (640, 480)
    videoWriter = cv2.VideoWriter('./static/img/video1.mp4', fourcc, fps, size)  # 最后一个是保存图片的尺寸
    for i in range(num):
        frame = cv2.imread(img_root + str(i) + ".jpg")
        videoWriter.write(frame)
    videoWriter.release()


c = np.loadtxt(r'./destine.txt')
num = int(c[1])
target=int(c[0])
move2target(target)
location=np.loadtxt("./location.txt",dtype=int)
add_frame_all(location[4] , location[5] , location[6] , location[7] , num , "./img2/")
trans2video_all("./img2/" , num)
trans2video_sound(target, "./img2/")
move2loca(num)
add_frame_part(location[0] , location[1] , location[2] , location[3] , "./pytorch-ssd-master/ssd_output_img/")
trans2video_end("./pytorch-ssd-master/ssd_output_img/")
