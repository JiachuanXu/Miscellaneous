# Decomp_List.py
# Produce list for Decompose_Image.py
# Usage: $ python Decomp_List.py <op_dir>
# Where <op_dir> is the output dir for decomposed images
# NOTE: MODIFY THE ls COMMAND EACH TIME!!! 
# By Jiachuan Xu, Feb, 23, 2018

import sys, os

# Confirm arguments
if len(sys.argv)!=2:
	print("Usage: $ python Decomp_List.py <op_dir>")
	exit()

# get current working dir 
cwd = os.getcwd()

# list the FITS files, including images and confidence maps
os.system("ls w*.fit > list")

image_list = open("list", 'r')
op_list = open("op_list", 'w')
op_dir = sys.argv[1]
# loop through list
for line in image_list.readlines():
	# <input image file> <output dir>
	content = "%s/%s %s\n"%(cwd, line[:-1], op_dir)
	op_list.write(content)
image_list.close()
op_list.close()
os.system("rm list")
