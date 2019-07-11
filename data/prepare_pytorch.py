#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file split data into training set , validation set and testing set 
and put each set in a separte csv file contains wave path and trascript text path 
"
@author: ASR EECE_19
"""
import os
import csv
from sklearn.model_selection import train_test_split

wavID_list = []
text_path = []
wav_path = []
path_csv = {}

with open('text.txt','r') as ifile:
    alltext = ifile.readlines()

for _trans in alltext:
    temp = _trans.split(' ')
    wav_ID = temp[0]
    wavID_list.append(temp[0])
    temp.remove(temp[0])
    wav_text = ' '.join(temp)
    text_path.append('data/txt/'+wav_ID+'.txt')

    ##splitting large text into multiple txt files 
    ## uncomment the following two lines to run it once
    #with open('./txt/'+wav_ID+'.txt','w') as writetext:
    #    writetext.write(wav_text)

wav_dir = './wav/'
spk_list = os.listdir(wav_dir)
for _id in wavID_list:
        k = _id.find('-')
        if _id[-2:] == '-s':
            wav_path.append('data/wav/speaker_'+_id[0:k]+'_s/'+_id+'.wav')
        elif _id[-2:] == '-n':
            wav_path.append('data/wav/speaker_'+_id[0:k]+'_n/'+_id+'.wav')
        else:
            wav_path.append('data/wav/speaker_'+_id[0:k]+'/'+_id+'.wav')


mgb_path = 'test-for-all/'
for i in os.listdir(mgb_path):
    print(str(i))
    txt = mgb_path+str(i)+'/txt_ar/'
    wav = mgb_path+str(i)+'/wav/'
    for fileid in os.listdir(wav):
        text_path.append('data/'+mgb_path+str(i)+'/txt_ar/'+fileid[0:-4]+'.txt')
        wav_path.append('data/'+mgb_path+str(i)+'/wav/'+fileid[0:-4]+'.wav')


t_train,t_valid,w_train,w_valid = train_test_split(text_path,wav_path,test_size = 0.1)
t_train,t_test,w_train,w_test = train_test_split(t_train,w_train,test_size = 0.1)

      
with open('temp/valid.csv','w') as out:
    writeCSV = csv.writer(out)
    for _ in range(len(t_valid)):
      writeCSV.writerow([w_valid[_],t_valid[_]])

with open('test.csv','w') as out:
    writeCSV = csv.writer(out)
    for _ in range(len(t_test)):
      writeCSV.writerow([w_test[_],t_test[_]])

size = int(len(t_train) / 5)
for i in range(5):

    t_part = t_train [i*size:i*size+size]
    w_part = w_train [i*size:i*size+size]
    with open('temp/train'+str(i+1)+'.csv','w') as out:
        writeCSV = csv.writer(out)
        for _ in range(len(t_part)):
            writeCSV.writerow([w_part[_],t_part[_]])