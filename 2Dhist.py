# 2Dhist.py 
# Plot the 2D Scatter-Histogram diagram
# z_spec v.s. z_phot(z_m2)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

BINS=60 # Number of bins
OFFSET = 0. # offset for bar bar3d chart
filename = "COSMOS2015_bc03.zout" # data

# Read in data 
data = np.genfromtxt(filename,names=True, dtype=None)
# Select sources with good redshift estimate
good_spec = np.logical_and(data['z_spec']>0.,data['z_spec']<10.)
good_m2 = np.logical_and(data['z_m2']>0.,data['z_m2']<10.)
good_both = np.logical_and(good_spec, good_m2)
index = np.where(good_both)
X = data['z_spec'][index]
Y = data['z_m2'][index]
# 3D histogram data
hist, xedges, yedges = np.histogram2d(X, Y, bins=BINS, range=[[0.,6.],[0.,6.]], normed=True)
xpos, ypos = np.meshgrid(xedges[:-1] + OFFSET, yedges[:-1] + OFFSET)
xpos = xpos.flatten('F')
ypos = ypos.flatten('F')
zpos = np.zeros_like(xpos)
# 2D histogram data: z_spec & z_m2
z_spec_hist, z_spec_xedges = np.histogram(X, bins=BINS, range=[0.,6.], normed=True)
z_m2_hist, z_m2_xedges = np.histogram(Y, bins=BINS, range=[0.,6.],normed=True)


# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left + width + 0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(8, 8))
#plt.suptitle("Scatter-Histogram of COSMOS2015 Field")

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# the scatter plot:
axScatter.scatter(X, Y, alpha=0.5)
xpos = np.arange(0.,6.,6./BINS)
ypos = np.arange(0.,6.,6./BINS)
# contour plot 
lev = np.geomspace(np.min(hist)+0.1,np.max(hist),20)
axScatter.contour(xpos, ypos, hist, levels=lev)

axScatter.set_xlim((0., 6.))
axScatter.set_ylim((0., 6.))
axScatter.set_xlabel(r"$z_{spec}$")
axScatter.set_ylabel(r"$z_{m2}$")

bins = np.arange(0., 6. + 6./BINS, 6./BINS)
axHistx.hist(X, bins=bins)
axHisty.hist(Y, bins=bins, orientation='horizontal')

axHistx.set_xlim(axScatter.get_xlim())
axHistx.set_xticks([])
axHisty.set_ylim(axScatter.get_ylim())
axHisty.set_yticks([])

plt.savefig("2DScatterHist.png",dpi=350)