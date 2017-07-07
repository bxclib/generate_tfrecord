# -*- coding: utf-8 -*- 
import numpy as np
import os
import tensorflow as tf
from PIL import Image
from settings import *
from utils import *
mkdir(tf_dir)
TFwriter = tf.python_io.TFRecordWriter(tf_dir+tf_name)
counter=0
error=0
succ=0
for className in os.listdir(root):
    if className not in matching_name:
	print "matching name loss,please check your data catecory"
	
print "The status will be printed every "+str(print_interval)+" pictures"
for className in os.listdir(root):
    label=matching_name[className]
    print "className"+className
    print "is"
    print "label"+str(label)
    classPath = root+"/"+className+"/"
    for parent, dirnames, filenames in os.walk(classPath):
        for filename in filenames:
            imgPath = classPath+"/"+filename
            try:
            	img = Image.open(imgPath)
		exec(pre_process)
            	counter=counter+1
		succ=succ+1
	    	if counter==print_interval:
			counter=0
			print "now is processing"
			print (imgPath)
            		print (img.size,img.mode)
			print "succeed wrote "+str(succ)+" files"
            	imgRaw = img.tobytes()
            	example = tf.train.Example(features=tf.train.Features(feature={
                	"label":tf.train.Feature(int64_list = tf.train.Int64List(value=[label])),
                	"img":tf.train.Feature(bytes_list = tf.train.BytesList(value=[imgRaw]))
            	}) )
                TFwriter.write(example.SerializeToString())
	    except:
		error=error+1
print "finish all "+str(succ)+" files"
print str(error)+" files failed."
TFwriter.close()
