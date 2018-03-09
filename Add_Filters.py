# Add_Filters.py
# Add filter into filter library of photo-z softwares
# The filter file should only have two columns: wavelength transmitance

import numpy as np 

### Edit the following info
filter_name = "y_HSC.txt" # name of the corresponding res file 
header_line = 0 # line of header in the res file 
filter_lib = "../FILTER.RES.latest" # lib file of filter
filter_info = "../FILTER.RES.latest.info" # info file of the lib 
wavelength = 'wlen' # dic for wavelength in column name 
transmit = 't' # dic for transmitance in column name 
lib_format = "%5d\t%f\t%f\n" # the format of the lib

# read filter file
res = np.genfromtxt(filter_name, names=True, skip_header=header_line,dtype=None)
# total lines
tot_line= len(res)
print(filter_name+": %d lines"%tot_line)

# filter library
op = open(filter_lib,'a') # append
op.write("%5d %s\n"%(tot_line, filter_name)) ## EDIT THE HEADER HERE 
for i in np.arange(0,tot_line,1):
	op.write(lib_format%(i+1, res[wavelength][i], res[transmitance][i])) ## ALSO EDIT FORMAT HERE
op.close()

# filter info
info = open(filter_info,'a+')
info.seek(0)
seq = len(info.readlines())
info.write("%5d %s\n"%(seq+1, filter_name))
info.close()
