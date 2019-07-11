#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ASR EECE_19
"""

"""
This file is used to map Arabic characters of each transcript into English characters 
"""
import os

char_map_str = """
A ء
B آ
C أ
D ؤ
E إ
F ئ
G ا
H ب
I ة
J ت
K ث
L ج
M ح
N خ
O د
P ذ
Q ر
R ز
S س
T ش
U ص
V ض
W ط
X ظ
Y ع
Z غ
a ف
b ق
c ك
d ل
e م
f ن
g ه
h و
i ى
j ي
k ً
l ٌ
m ٍ
n َ
o ُ
p ِ
q ّ
r ْ
s ـ
"""
out_sen = []
char_seq = []
char_map = {}
for line in char_map_str.strip().split('\n'):
    en, ar = line.split()
    char_map[ar] = en

for i in range(134,161):

    outpath = './'+str(i)+'/txt_ar/'
    try:  
        os.mkdir(outpath);
    except OSError:  
        print ("Creation of the directory %s failed" % outpath)
    else:  
        print ("Successfully created the directory %s" % outpath)

    txtpath = './'+str(i)+'/txt/'
    txtlist = os.listdir(txtpath)
    for txtfile in txtlist: 
        with open(txtpath+txtfile,'r') as ifile:
            isentence = ifile.readlines()

        for sen in isentence:
            for j in range(len(sen)):
                if sen[j] == ' ' or sen[j] == '*' or sen[j] == '\n':
                    char_seq.append(sen[j])
                else:
                    char_seq.append(char_map[sen[j]])
                    
            out_sen.append(''.join(char_seq))
            char_seq.clear()

        with open(outpath+txtfile,'w') as ofile:
            for _ in out_sen:
                ofile.write(_)
        out_sen.clear()
