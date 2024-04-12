import numpy as np
import matplotlib.pyplot as plt
def derivacija(f, x, epsilon = 0.01, metoda = 'three-step'):
    a = x
    if metoda == 'three-step':
        d = (f(a + epsilon) - f(a - epsilon)) / (2.*epsilon)
        return round(d,4)

    elif metoda == 'two-step':
        d = (f(a + epsilon) - f(a)) / (epsilon)
        return round(d,4)

def f1(x):
    return x**3.

def f2(x):
    return np.sin(x)

#der = derivacija(f1, 2.)
#der = derivacija(f2, 0.)
#print(der)


def der_granice(f,fa,d,g,epsilon = 0.5, metoda = 'three-step'):
    x = d
    def three():
        der = (f(x + epsilon) - f(x - epsilon)) / (2.*epsilon)
        #derivacije.append(round(der,4))
        return der

    def two():
        der = (f(x + epsilon) - f(x)) / (epsilon)
        #derivacije.append(round(der,4))
        return der
    listad = []
    listat = []
    listada = []
    while x>= d and x<=g:
        listat.append(x)
        if metoda == 'three-step':
            listad.append(three())

        elif metoda == 'two-step':
            listad.append(two())
        listada.append(fa(x))
        x += 0.1


    
    #print(tocke,derivacije)
    #print(tocke,derivacije_a)
    plt.plot(listat,listad,'o',color = 'purple',markersize = 5)
    plt.plot(listat,listada)

def f1(x):
    return x**3.

def f1a(b):
    return 3.*b**2.

def f2(x):
    return np.sin(x)

def f2a(x):
    return np.cos(x)

def f3(x):
    5.*x**3. - 2.*x**2. + 2.*x -3.

def f3a(x):
    15.*x**2. -4.*x +2.

#der_granice(f1,f1a,-5.,5.,50.)

der_granice(f2,f2a, -2.,2.)

plt.show()