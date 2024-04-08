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

def der_granice(f,fa,d,g,epsilon = 1, metoda = 'three-step'):
    tocke = []
    derivacije = []
    derivacije_a = []
    for x in np.linspace(d,g):
        b = x
        derivacije_a.append(fa(b))
    N = int(abs(g-d)/epsilon)
    for x in np.linspace(d,g,N):
        tocke.append(x)
        a = x
        derivacije_a.append(fa(x))
        if metoda == 'three-step':
            der = (f(a + epsilon) - f(a - epsilon)) / (2.*epsilon)
            derivacije.append(round(der,4))

        elif metoda == 'two-step':
            der = (f(a + epsilon) - f(a)) / (epsilon)
            derivacije.append(round(der,4))
    print(tocke,derivacije)
    plt.plot(tocke,derivacije,'o',color = 'purple',markersize = 1)
    plt.plot(tocke,derivacije_a)
    plt.show()

def f1(x):
    return x**3.

def f1a(b):
    return 3.*b**2.

def f2(x):
    return np.sin(x)

def f2a(b):
    return np.cos(b)

#der_granice(f1,f1a,-5.,5.,50.)
der_granice(f2,f2a,0.,10.)
