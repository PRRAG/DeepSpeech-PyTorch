### This file is to show how to prepare data for training pytorch ###

 steps to prepare data 
 1)  'prepare-mgb-data.py' This file used to remove audio waves of less than 4 seconds because most of them are corrupted data 
 2)  'convert_ar_en.py' This file is used to map Arabic characters of each transcript into English characters  
 3)  'prepare_pytorch.py' This file shuffle and split data into training set , validation set and testing set , 
and put each set in a separate csv file contains wave path and trascript path 

Mapping of charcters 
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