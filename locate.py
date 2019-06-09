# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:50:49 2019

@author: msq
"""

import wave
from pyaudio import PyAudio,paInt16
import cv2


cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(0)
cap3 = cv2.VideoCapture(3)
while 1:
    _, frame = cap.read()
    _, frame2 = cap2.read()
    _, frame3 = cap3.read()
    cv2.imshow('frame',frame)
    cv2.imshow('frame2',frame2)
    cv2.imshow('frame3',frame3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()

