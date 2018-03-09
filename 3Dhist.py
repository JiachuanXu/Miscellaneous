# 3Dhist.py
# Plot 3D histogram 
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np 

BINS = 60
OFFSET = 0.
WIDTH = 6/BINS*0.9

fig = plt.figure()
fig.suptitle("Redshift Distribution of COSMOS2015 Field (Slice)")
ax = fig.gca(projection='3d')

# Read in data 
data = np.genfromtxt("COSMOS2015_bc03.zout",names=True, dtype=None)
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


dx =  WIDTH*np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

# Plot the 3D bar chart
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', alpha=0.3, cmap=cm.coolwarm)

# Plot projections of the histogram for each dimension. 
ax.bar(z_spec_xedges[:-1], z_spec_hist*3, zs=7., zdir='y', align='edge',width=6./BINS, alpha=0.7)
ax.bar(z_m2_xedges[:-1], z_m2_hist*3, zs=-1., zdir='x', align='edge', width=6./BINS, alpha=0.7)

ax.set_xlim(-1., 7.)
ax.set_ylim(-1., 7.)
ax.set_xticks(np.arange(0.,7.,1.))
ax.set_yticks(np.arange(0.,7.,1.))

ax.set_xlabel(r'$z_{spec}$')
ax.set_ylabel(r'$z_{m2}$')
ax.set_zlabel('Sample Density')

fig.savefig("3DHistogram.png",dpi=350)