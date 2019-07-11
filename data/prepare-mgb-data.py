#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:15:48 2019

@author: ASR EECE_19
"""
"""
This file used to remove audio waves of less than 4 seconds to improve training 

"""
import os
import wave

data_path = './test-for-all/'
wavID_list = []
final_trans = []

for i in os.listdir(data_path):
    print(str(i))
    txt_path = data_path+str(i)+'/txt_ar/'
    wav_path = data_path+str(i)+'/wav/'
    for fileid in os.listdir(txt_path):
        audio = wave.open(wav_path+fileid[0:-4]+'.wav')
        duration = float(audio.getnframes()) / audio.getframerate()
        if(duration >= 4):
            wavID_list.append(fileid[0:-4])
        else:
            os.remove(wav_path+fileid[0:-4]+'.wav')
            os.remove(txt_path+fileid[0:-4]+'.txt')
            print(wav_path+fileid[0:-4]+" =============> Removed!")
            continue
        
    