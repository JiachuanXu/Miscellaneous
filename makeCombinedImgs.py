from matplotlib.colors import LogNorm
from astropy.io import fits
from astropy.wcs import WCS
from astropy import units as u
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import zscale as zs
import sys


def plot_image(infile,outfile,ext):
	print(infile,outfile,ext)
	
	fig = plt.figure(figsize=(10,10))
	ax = fig.gca()

	fig.suptitle('%s' % (outfile), fontsize=15)

	try: hdu = fits.open(infile)
	except: 
		print("cannot open file!!! ")

	#print hdu[0].header

	image_data = hdu[ext].data

	#ax.axes.get_xaxis().set_visible(False)
	#ax.axes.get_yaxis().set_visible(False)

	image_data[image_data<0] = 1e-20

	clow,chigh = zs.zscale(image_data,nsamples=2000)

		
	# percentage
	'''
	clow = np.percentile(image_data,50)
	chigh = np.percentile(image_data,60)
	'''
	#plt.imshow(image_data, cmap='afmhot',interpolation='none', norm=LogNorm(),clim=[clow,chigh])
	plt.imshow(image_data, cmap='binary',interpolation='none', clim=[clow,chigh], origin='lower')
	#plt.imshow(image_data, cmap='gray',interpolation='nearest', clim=[clow,chigh])

	
	#fig.set_tight_layout(True)
	plt.savefig(outfile, pad_inches = 0.)
	#plt.show()	
	#exit()

