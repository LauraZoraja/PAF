import particle as prt
import numpy as np
import matplotlib.pyplot as plt

listae = []
listat = []
for t in np.linspace (0.000001,0.1,500):
    p1 = prt.particle(0,0,10,60)
    D_a = (((p1.v0)**2)/(p1.ay))*np.sin(2*p1.kut)
    p1.range(t)
    err = (abs(D_a - p1.D_n)/D_a)*100
    listae.append(err)
    listat.append(t)
    p1.reset()

plt.plot(listat,listae)
plt.xlabel('dt [s]')
plt.ylabel('Absoute relative error [%]')
text = '$(Err) = \\frac{|D_{analitical} - D_{numerical}|}{D_{analitical}}\\cdot(100\\%)$'
plt.text(0.001,9,text,fontsize = 15)
plt.show()