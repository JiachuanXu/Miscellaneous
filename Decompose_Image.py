# Decompose_Image.py 
# To decompose a multi-extension FITS image into different images
# Usage: $ python Decompose_Image.py <list>
#	Where lists include input filename and output dir:
#		''' list file sample
#			/media/xu/images/w19960218_02203.fits /media/xu/udisk
#			......
#		'''
# And would also copy some parameters from primary header to extensions
# headers, see variable "PARAM"
# By Jiachuan Xu, Feb, 23, 2018

from astropy.io import fits
import numpy as np 
import sys

# Confirm the arguments
if len(sys.argv)!=2:
	print("Usage: $ python Decompose_Image.py <list>\n\
		Where list include input filename and output dir.")
	exit()

# The following parameters will be copied from 
# primary header to extension headers
PARAM = ['RADESYS','EQUINOX','TRACKSYS','AMSTART','AMEND','NINT',\
'EXP_TIME','NEXP','READINT','NREADS']

# open and loop through list
input_list = open(sys.argv[1],'r')
for line in input_list.readlines():
	ip_filename = line.split(" ")[0]
	fn_kernal = ip_filename.split("/")[-1].split(".")[0]
	print("Processing %s.fit ..." % fn_kernal)
	op_dir = line.split(" ")[1][:-1] # delete the '\n'
	# open FITS image, readonly by default
	image = fits.open(ip_filename)
	# get number of extensions
	ext = len(image)
	primary = image[0].header
	# loop through extensions
	for i in np.arange(1, ext, 1):
		# append the params from primary header to exts' headers
		for param in PARAM:
			image[i].header.set(param,primary[param])
			image[i].header.comments[param] = primary.comments[param]
		# construct output file name
		op_filename = "%s/%s_%d.fit"%(op_dir, fn_kernal, i)
		# write the new sub-image with exts' headers
		hdu_p = fits.PrimaryHDU(np.array([]), header=image[i].header)
		hdu_i = fits.ImageHDU(image[i].data,header=image[i].header)
		nhdul = fits.HDUList([hdu_p, hdu_i])
		nhdul.writeto(op_filename)
	image.close()
