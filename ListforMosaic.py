# ListforMosaic.py
# Produce a list for mosaic, exclude bad-quality image from the list 
# Usage: $ python ListforMosaic.py <image quality list>
# image quality list: list for bad quality image, format like this
# ''' image quality list sample: file://PATH/filename # comment reason
#     file:///media/xu/Jiachuan_HFSplus/check_images/BOSS1441_POINT1/H/w20140314_01512_st_2.fit # crush
#     file:///media/xu/Jiachuan_HFSplus/check_images/BOSS1441_POINT1/H/w20140314_01557_st_1.png # blur
# '''
# NOTE: MODIFY THE ls COMMAND, EXTS and FILE "KERNAL" EACH TIME, AND THE FILENAME IN image quality list 
# 		MUST BE COORDINATE WITH Decompose_Image.py 
# By Jiachuan Xu, Feb, 24, 2018

import sys, os
import numpy as np 

# retrive info about image from image filename 
def get_image_info(name):
	seq = int(name.split(".")[0][-1]+\
		name.split("_")[0][1:]+\
		name.split("_")[1]) # generate a sequence number
	return seq

# confirm arguments
if len(sys.argv)!=2:
	print("Usage: $ python ListforMosaic.py <image quality list>")
	exit()

EXTS = 4 # number of extensions

# open image quality list
IQ_list = open(sys.argv[1], 'r')
bad_im = np.zeros(0)
# extract file "kernal", say, 22014031401557
for line in IQ_list.readlines():
	temp = line.split('#')[0]
	temp = temp.split('/')[-1]
	seq = get_image_info(temp)
	bad_im = np.append(bad_im, seq)
IQ_list.close()

# loop through extensions, ls files into a list, and exclude bad-quality images
for i in np.arange(1, EXTS+1, 1):
	imlist = "image_%d.input"%i
	cflist = "conf_%d.input"%i 
	os.system("ls w*_st_%d.fit > %s" % (i, imlist))
	os.system("ls w*_st_conf_%d.fit > %s" % (i, cflist))
	# processing image list
	image_list = open(imlist, 'r')
	new_image_list = open("new_im_list",'w') # temporaty file 
	for line in image_list.readlines():
		seq = get_image_info(line)
		if seq not in bad_im:
			new_image_list.write(line)
	image_list.close()
	new_image_list.close()
	# rename the temporary file
	os.system("rm %s"%imlist)
	os.system("mv new_im_list %s"%imlist)
	# processing conf list 
	conf_list = open(cflist, 'r+')
	new_conf_list = open("new_cf_list",'w') # temporaty file 
	for line in conf_list.readlines():
		seq = get_image_info(line)
		if seq not in bad_im:
			new_conf_list.write(line)
	conf_list.close()
	new_conf_list.close()
	# rename the temporary file
	os.system("rm %s"%cflist)
	os.system("mv new_cf_list %s"%cflist)