import numpy as np
import os

BACK_SIZE = np.array([32,64,128,256])
BACK_FILTERSIZE = np.array([3,6,9])
FILTER_NAME = ["config/gauss_1.5_3x3.conv","config/gauss_2.0_3x3.conv","config/gauss_2.0_5x5.conv","config/gauss_2.5_5x5.conv","config/gauss_3.0_5x5.conv","config/gauss_3.0_7x7.conv","config/gauss_4.0_7x7.conv","config/gauss_5.0_9x9.conv"]

for param1 in BACK_SIZE:
	for param2 in BACK_FILTERSIZE:
		for param3 in FILTER_NAME:
			fil = param3.split('/')[1]
			fil = fil.split('.')[0]+'.'+fil.split('.')[1]
			cmd = "sex BOSS1441_POINT1_J.fits -c config/IPAC_J.sex -BACK_SIZE %d -BACK_FILTERSIZE %d -FILTER_NAME %s -CHECKIMAGE_NAME check_image/APER_J_4as_%d-%d_%s.fits,check_image/XOBJ_J_4as_%d-%d-%s.fits,check_image/BG_J_4as_%d-%d-%s.fits -CATALOG_NAME catalog/BOSS1441_J_4as_%d-%d-%s.cat"%(param1,param2,param3,param1,param2,fil,param1,param2,fil,param1,param2,fil,param1,param2,fil)
			os.system(cmd)
