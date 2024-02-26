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
axis[0].plot(list(range(0,11)),listaa)
axis[1].plot(list(range(0,11)),listav)
axis[2].plot(list(range(0,11)),listax)
plt.show()