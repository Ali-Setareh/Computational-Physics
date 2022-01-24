import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
data=open('C:/Users/alise/Dropbox/simu in physics/Ex 4/7/data.txt','r')
a=data.readlines()
a=[int(i) for i in a]
a=np.asarray(a)
print(a)
steps=np.arange(1,16)
st=np.zeros(np.shape(steps)[0])
i=0
for item in steps:
    st[i]=a[i]/(4**item)
    i+=1

fig,ax=plt.subplots()
ax.plot(steps,a,'ro')
ax.plot(steps,st,'ro',color='b')
plt.yscale('log')
plt.xlabel('walk length')
plt.ylabel('unique walk numbers (log)')


slope, intercept, r_value, p_value, std_err = stats.linregress(steps,np.log10(a))
line1 = slope*steps+intercept
ax.plot(steps, 10**line1, 'r', label='number of SAW: y={:.2f}x+{:.2f}'.format(slope,intercept))

slope, intercept, r_value, p_value, std_err = stats.linregress(steps,np.log10(st))
line1 = slope*steps+intercept
ax.plot(steps, 10**line1, 'b', label='SAW/free walks: y={:.2f}x+{:.2f}'.format(slope,intercept))

plt.legend(fontsize=9)
plt.show()
data.close()