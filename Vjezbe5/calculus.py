def derivacija(f, x, epsilon = 0.1, metoda = 'three-step'):
    a = x
    if metoda == 'three-step':
        d = (f(a + epsilon) - f(a - epsilon)) / (2.*epsilon)
        return d

    elif metoda == 'two-step':
        d = (f(a + epsilon) - f(a)) / (epsilon)
        return d

def f(x):
    return x**3.

der = round(derivacija(f, 45.),2)
dera = 3.*45.**2.

print(der,dera)