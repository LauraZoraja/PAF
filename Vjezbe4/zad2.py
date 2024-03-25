import particle as prt
import numpy as np
import matplotlib.pyplot as plt
p1 = prt.particle(0,0,10,60)
p2 = prt.particle(0,0,10,60)
p3 = prt.particle(0,0,10,60)
D_a = (p1.v0)**2/p1.ay * np.sin(2*p1.kut)
p1.range() #dt=0.001
D_n1 = p1.listaxi[-1]
Err_1 = D_n1 - D_a
#print(Err_1)

p2.range(0.01)
D_n2 = p2.listaxi[-1]
Err_2 = D_n2 - D_a
#print(Err_2)

p3.range(0.1)
D_n3 = p3.listaxi[-1]
Err_3 = D_n3 - D_a
#print(Err_3)