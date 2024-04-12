import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
def derivacija_tocke(f, x, epsilon = 0.01, metoda = 'three-step'):
    a = x
    if metoda == 'three-step':
        d = (f(a + epsilon) - f(a - epsilon)) / (2.*epsilon)
        return round(d,4)

    elif metoda == 'two-step':
        d = (f(a + epsilon) - f(a)) / (epsilon)
        return round(d,4)


def derivacija_granice(f,fa,d,g,epsilon = 0.05, metoda = 'three-step',dva_epsilona = 'ne'):
    x = d
    def three(epsilon):
        der = (f(x + epsilon) - f(x - epsilon)) / (2.*epsilon)
        return der

    def two(epsilon):
        der = (f(x + epsilon) - f(x)) / (epsilon)
        return der
    listad = []
    listat = []
    listad2 = []
    listada = []
    while x>= d and x<=g:
        listat.append(x)
        if metoda == 'three-step':
            listad.append(three(epsilon))
            if dva_epsilona == 'da':
                listad2.append(three(epsilon = 0.5))
            else:
                pass

        elif metoda == 'two-step':
            listad.append(two(epsilon))
            if dva_epsilona == 'da':
                listad2.append(two(epsilon = 0.5))
            else:
                pass
        listada.append(fa(x))
        x += 0.1
    plt.plot(listat,listad,'o',color = 'purple',markersize = 3)
    plt.plot(listat,listad2,'o',color = 'red',markersize = 3)
    plt.plot(listat,listada)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Numericka derivacija')
    plt.text(-1,62,'$f(x) = 5x^3 - 2x^2 + 2x - 3$',{'fontsize': 13})
    plt.text(-1,55,'$ \\frac{df(x)}{dx} = 15x^2 - 4x + 2$',{'fontsize': 13},color = 'blue')
    plt.text(-0.5,48,'$\\varepsilon = 0.05$',{'fontsize': 13},color = 'purple')
    plt.text(-0.5,41,'$\\varepsilon = 0.5$',{'fontsize': 13},color = 'red')
    plt.show()

def f1(x):
    return x**3.

def f1a(x):
    return 3.*x**2.

def f2(x):
    return np.sin(x)

def f2a(x):
    return np.cos(x)

def f3(x):
    return 5.*x**3. - 2.*x**2. + 2.*x -3.

def f3a(x):
    return 15.*x**2. - 4.*x + 2.

derivacija_granice(f3,f3a, -2.,2.,dva_epsilona = 'da')

def pravokutna_integracija(f,d,g,N):
    def sume(f,d,g,N):
        dx = abs(float(g)-float(d))/N
        sumad = 0
        sumag = 0
        for i in range(N):
            sumag += f((i+1)*dx)*dx
            sumad += f(i*dx)*dx
        print('Gornja suma iznosi {}, a donja {}.'.format(round(sumag,4),round(sumad,4)))
    listad = []
    listag = []
    listam = []
    listaN = []
    listaia = []
    sumag = 0
    sumad = 0
    for n in np.arange(50,N,50):
        dx = abs(float(g)-float(d))/n
        listaia.append(Fraction(11,3))
        listaN.append(n)
        for i in range(n):
            sumag += f((i+1)*dx)*dx
            sumad += f(i*dx)*dx
        listad.append(sumad)
        listag.append(sumag)
        listam.append(abs(sumag-sumad)/2 + sumad)
        sumag=0
        sumad=0
    plt.plot(listaN,listag,'o',markersize = 3)
    plt.plot(listaN,listad,'o',markersize = 3)
    plt.plot(listaN,listam,'o',markersize = 3)
    plt.plot(listaN,listaia)
    plt.text(-1,62,'$f(x) = 2x^2 + 3$',{'fontsize': 13})
    plt.title('Pravokutna integracija')
    plt.xlabel('Nsteps')
    plt.ylabel('Integral')
    plt.show()
    sume(f,d,g,N)


def f4(x):
    return 2*x**2 + 3
pravokutna_integracija(f4,0.,1.,1000)

def trapezna_integracija(f,d,g,N):
    integral = 0
    listai = []
    listaN = []
    listaia = []
    for n in np.arange(50,N,50):
        dx = (abs(float(g)-float(d)))/n
        listaN.append(n)
        listaia.append(11./3.)
        for i in range(n):
            integral += (f((i+1)*dx) + f(i*dx))
        listai.append(integral*(dx/2))
        integral = 0
    plt.plot(listaN,listai,'o',markersize = 3)
    plt.plot(listaN,listaia)
    plt.text(-1,62,'$f(x) = 2x^2 + 3$',{'fontsize': 13})
    plt.title('Trapezna integracija')
    plt.xlabel('Nsteps')
    plt.ylabel('Integral')
    plt.show()

trapezna_integracija(f4,0.,1.,1000)