import numpy as np 
from astropy.stats import sigma_clip
filename = "OUTPUT/COSMOS2015_bc03.zout"
survive_name = "OUTPUT/COSMOS2015_bc03_survive.zout"
clipout_name = "OUTPUT/COSMOS2015_bc03_clipout.zout"

def notclipped(inp):
	mean = np.mean(inp)
	dev = np.std(inp)
	mask = []
	for i in inp:
		if (i<mean-3*dev) and (i>mean+3*dev):
			mask = np.append(mask, True)
		else:
			mask = np.append(mask, False)
	return mask

def isgalaxy(z_spec):
	mask = []
	for i in z_spec:
		if (i>0)and(i<10):
			mask = np.append(mask, True)
		else:
			mask = np.append(mask, False)
	return mask


data = np.genfromtxt(filename, names=True, dtype=None)
galaxy_list = np.array([],dtype=int)
for i in np.arange(0,len(data),1):
	if (data['z_spec'][i]>0.) and (data['z_spec'][i]<10.):
		galaxy_list = np.append(galaxy_list, int(i))
new_column = abs(data['z_m2'][galaxy_list]-data['z_spec'][galaxy_list])/(data['z_spec'][galaxy_list]+1.0)
new_dtype = np.dtype(data.dtype.descr+[('accuracy','float64')])
new_data = np.zeros(len(galaxy_list), dtype = new_dtype)
for i in data.dtype.names:
	new_data[i]=data[i][galaxy_list]
new_data['accuracy']=new_column

filtered_data = sigma_clip(new_data['accuracy'], sigma=3, iters=None)
survive_size = len(galaxy_list)-np.sum(filtered_data.mask)
clipout_size = np.sum(filtered_data.mask)
survive_data = np.zeros(survive_size, dtype = new_dtype)
clipout_data = np.zeros(clipout_size, dtype = new_dtype)
survive_ct = -1
clipout_ct = -1
for i in np.arange(0,len(galaxy_list),1):
	if ~filtered_data.mask[i]:
		survive_ct += 1
		for j in new_data.dtype.names:
			survive_data[j][survive_ct] = new_data[j][i]
	else:
		clipout_ct += 1
		for j in new_data.dtype.names:
			clipout_data[j][clipout_ct] = new_data[j][i]


print("filtered data: %.3f +- %.3f"%(np.mean(survive_data['accuracy']), np.std(survive_data['accuracy'])))

np.savetxt(survive_name,survive_data,fmt="%d %.4f %.3f %.3f %e %.3f %e %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.3f %d %e %.3f %.3f %.3f %.3f", header="id z_spec z_a z_m1 chi_a z_p chi_p z_m2 odds l68 u68  l95 u95  l99 u99  nfilt q_z z_peak peak_prob z_mc accuracy")
np.savetxt(clipout_name,clipout_data,fmt="%d %.4f %.3f %.3f %e %.3f %e %.3f %.3f %.3f %.3f %.3f %.3f %.3f %.3f %d %e %.3f %.3f %.3f %.3f", header="id z_spec z_a z_m1 chi_a z_p chi_p z_m2 odds l68 u68  l95 u95  l99 u99  nfilt q_z z_peak peak_prob z_mc accuracy")