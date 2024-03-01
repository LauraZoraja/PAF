import matplotlib.pyplot as plt

F = float(input('Unesite iznos sile u Newtonima: '))
m = float(input('Unesite iznos mase u kilogramima: '))
listaa = []
listax = []
listav = []
for t in range(0,11):
    a = F/m
    x = (a*t**2)/2
    v = a*t
    listaa.append(a)
    listax.append(x)
    listav.append(v)

figure, axis = plt.subplots(3,1)
axis[0].plot(list(range(0,11)),listaa,'r')
axis[1].plot(list(range(0,11)),listav,'b')
axis[2].plot(list(range(0,11)),listax,'g')
axis[0].set_xlabel('t [s]')
axis[0].set_ylabel('a [m/$s^2$]')
axis[1].set_xlabel('t [s]')
axis[1].set_ylabel('v [m/s]')
axis[2].set_xlabel('t [s]')
axis[2].set_ylabel('x [m]')
plt.tight_layout()
plt.show()