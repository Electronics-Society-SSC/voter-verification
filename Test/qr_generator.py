# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:53:43 2019

@author: pauljr
"""
# Some sample output here: https://github.com/p-j-r/voter-verification/issues/1#issue-539113485

import os
import qrcode
from random import randint,choice

course=['bphy','bche','phil','sans','econ','bapa','bscp']
count=1
while(count<=1200):          # Generate 1200 ID's
    yy=str(randint(17,19))   # Year Component: 17, 18, 19
    cr=choice(course)        # One of the course codes listed
    no=str(randint(1,60))    # Serial/ Roll No.
    if (len(no)==1):
        no="0"+no            # Append 0, if single digit number
    data =yy+cr+"0"+no       # eg: 19BPHY060
    
    filename = data+".png"       
    
    path="C:\\Users\alpha\Documents\QR"
    fullname=os.path.join(path,filename)
    img = qrcode.make(data)
    img.save(fullname)
    
    count=count+1
    
#print(count)
# This program generates about 780 images (tested on Windows). I guess it is because id is getting repeated, 
# and Windows is preventing same filenames from getting saved or it's being replaced.
