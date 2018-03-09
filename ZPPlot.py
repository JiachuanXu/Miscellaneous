# ZPPlot.py 
# Plot zero-point calibration figure
# read ascii form, should include column of 'diff' and 'band corr'

import matplotlib.pyplot as plt 
import numpy as np 

# Edit the band info
band = 'K'
corr_band = 'k_corr'
corr_band_err = 'k_msigcom'

# Edit the following info if needed
filename = "%s_Combine_3.txt"%band 
tot_title = "Zero-Point Calibration for BOSS1441: %s band"%band
opname = "ZP_%s.png"%band

# read data
data = np.genfromtxt(filename, names=True, dtype=None)
x = data[corr_band]
y = data['diff']
dx = data[corr_band_err]
# instrumental magnitude
v_4 = data['v_aper_4_01']
verr_4 = data['err_4as_01']
dy = y*np.sqrt((dx/x)**2.+(verr_4/v_4)**2.)
ZP = np.mean(data['diff'])
ZP_ERR = np.std(data['diff'])
# x axis array
x_line = np.arange(x.min(),x.max()+0.2,0.2)

# ---------------------------------------------------------------------
# plot figure
figure = plt.figure(figsize=(10,8))
figure.suptitle(tot_title,fontsize=22)
# define axis
ax_diff = plt.axes((0.2,0.1,0.65,0.3))
ax_vs = plt.axes((0.2,0.4,0.65,0.5))

# set function need plotting

# axis 1: difference
ax_diff.errorbar(x,y,xerr=dx,yerr=dy,label="Sample (%d)"%data.size,fmt='o')
ax_diff.axhline(ZP,label="Zero-Point",c='r',linestyle="--")
ax_diff.axhline(ZP-ZP_ERR,label=r"1 $\sigma$ deviation",c='r',linestyle=":")
ax_diff.axhline(ZP+ZP_ERR,c='r',linestyle=":")
# set axis
ax_diff.set_xlim(x.min()-0.1,x.max()+0.1)
ax_diff.set_xlabel(r'$%s_{2MASS}$ [Vega mag]'%band,fontsize=16)
ax_diff.set_ylabel(r'$%s_{UKIRT}-%s_{2MASS}$ [Vega mag]'%(band,band),fontsize=16)

# axis 2: mag-mag
ax_vs.errorbar(x,v_4,xerr=dx,yerr=verr_4,label="Sample (%d)"%data.size,fmt='o')
ax_vs.plot(x_line,x_line-ZP,label=r"$%s_{UKIRT}$=$%s_{2MASS}$-$(%.3f\pm%.3f)$"%(band,band,ZP,ZP_ERR),c='r',linestyle="--")
ax_vs.plot(x_line,x_line-ZP-ZP_ERR,label=r"1 $\sigma$ deviation",c='r',linestyle=":")
ax_vs.plot(x_line,x_line-ZP+ZP_ERR,c='r',linestyle=":")
# set axis
ax_vs.set_xlim(x.min()-0.1,x.max()+0.1)
ax_vs.set_xticks([])
ax_vs.set_ylabel(r'$%s_{UKIRT}$ [Vega mag]'%band,fontsize=16)
ax_vs.legend(fontsize=12)

figure.savefig(opname,dpi=350)