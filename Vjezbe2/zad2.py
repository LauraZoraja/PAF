import matplotlib.pyplot as plt
import numpy as np

v0 = float(input('Unesite iznos pocetne brzine: '))
kuts = float(input('Unesite iznos kuta otklona u stupnjevima: '))
g = 9.81
kutr = np.radians(kuts)
listax = []
listay = []
for t in range(0,11):
    x = v0*np.cos(kutr)*t
    y = v0*np.sin(kutr)*t - 0.5*g*t**2
    listax.append(x)
    listay.append(y)

figure, axis = plt.subplots(3,1)
axis[0].plot(listay,listax,'r')
axis[1].plot(list(range(0,11)),listax,'b')
axis[2].plot(list(range(0,11)),listay,'g')
axis[0].set_xlabel('y [m]')
axis[0].set_ylabel('x [m]')
axis[1].set_xlabel('t [s]')
axis[1].set_ylabel('x [m]')
axis[2].set_xlabel('t [s]')
axis[2].set_ylabel('y [m]')
plt.tight_layout()
plt.show()