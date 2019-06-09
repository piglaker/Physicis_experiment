# -*- coding: utf-8 -*-
#! /usr/bin/env python3
"""
Created on Fri Jun  7 14:00:42 2019

@author: msq
"""
import numpy as np
from flask import Flask, jsonify, abort, request, redirect, render_template,send_from_directory
import os
app = Flask(__name__, static_url_path = "")

@app.route('/showStar', methods=['GET', 'POST'])
def showStar():
    ok=int(np.loadtxt(r'./ok.txt',dtype=int))
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
    goal=score[0]+score[1]+score[2]+score[3]+score[4]+score[5]
    print(ok)
    if request.method == 'POST' or request.method == 'GET':
        
        result = {
            'ok':int(ok),
	        'grade':int(goal),
            'result0': int(score[0]),
            'result1': int(score[1]),
            'result2': int(score[2]),
            'result3': int(score[3]),
            'result4': int(score[4]),
            'result5': int(score[5]),
            'error1': int(error[0][0]),
            'error2': int(error[0][1]),
            'error3': int(error[0][2]),
            'error4': int(error[0][3]),
            'error5': int(error[0][4]),
            'video0':"/img/alphapose-video1/AlphaPose_video1.mp4"
        }
        return jsonify(result)
@app.route('/video1', methods=['GET', 'POST'])
def video1():
   
    if request.method == 'POST' or request.method == 'GET':
        
        result = {
            'video1':"/img/alphapose-video2/AlphaPose_video2.mp4"#第一个视频
            
        }
        return jsonify(result)
@app.route('/video2', methods=['GET', 'POST'])
def video2():
   
    if request.method == 'POST' or request.method == 'GET':
        
        result = {
            'video1':"/img/alphapose-video2/AlphaPose_video2.mp4"#第2个视频
            
        }
        return jsonify(result)
@app.route('/video3', methods=['GET', 'POST'])
def video3():
   
    if request.method == 'POST' or request.method == 'GET':
        
        result = {
            'video1':"/img/video4.mp4"#第3个视频
            
        }
        return jsonify(result)
@app.route('/video4', methods=['GET', 'POST'])
def video4():
    if request.method == 'POST' or request.method == 'GET':
        print(1)
        result = {
            'video1':"/img/video3.mp4"#第4个视频
            
        }
        return jsonify(result)
@app.route('/video5', methods=['GET', 'POST'])
def video5():
   
    if request.method == 'POST' or request.method == 'GET':
        
        result = {
            'video1':"/img/1.mp4"#第5个视频
            
        }
        return jsonify(result)

@app.route("/")
def main():

    return render_template("2.html")   
if __name__ == '__main__':


    app.run(debug=True, host= '0.0.0.0')
