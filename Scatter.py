import numpy as np 
import matplotlib.pyplot as plt

filename = "K_4ac_64-3.txt"
data = np.genfromtxt(filename, dtype=None, names=True)
x = np.arange(data['kcorr'].min(),data['kcorr'].max()+0.1,0.1)

fig = plt.figure(figsize=(10,10))
fig.suptitle("Zero-Point Correction-K (Vega)")
plt.errorbar(data['kcorr'],data['v_aper_01'],xerr=data['k_msigcom'], yerr=data['ver_aper_01'], fmt='.k',label="Sample (%d)"%data['v_aper_01'].size)
plt.plot(x,x-24.9874,color='r',linestyle='--',label=r"$k_{ins}=k_{corr}-(24.9874\pm0.0529)$")
plt.plot(x,x+0.052903-24.9874,color='r',linestyle=':')
plt.plot(x,x-0.052903-24.9874,color='r',linestyle=':')
plt.xlabel("k corrected magnitude-2MASS")
plt.ylabel("k instrumental magnitude-UKIRT")
plt.legend(loc="lower right")
plt.savefig("errorbar_K.png",dpi=350)
