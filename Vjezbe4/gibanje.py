import particle as prt
import numpy as np
p1 = prt.particle(0,0,10,45)
D_a = (p1.v0)**2/p1.ay * np.sin(2*p1.kut)
print(D_a)
p1.range()
D_n = p1.listaxi[-1]

Err = D_n - D_a
print(Err)

#ima ostupanja od analitickog rjesenja, ali odstupanje iznosi 0.009, pa je gotovo zanemarivo