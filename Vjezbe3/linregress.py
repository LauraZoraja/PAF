def lingress():
    import matplotlib.pyplot as plt
    import numpy as np

    M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
    phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]
    sum_a = 0 
    Dt1 = [M_el / phi_el for M_el, phi_el in zip(M,phi)]

    a1 = [(M_el * phi_el) / (phi_el)**2 for M_el, phi_el in zip(M,phi)]
 
    for el in a1:
        sum_a += el

    a = sum_a/len(a1)
    print(a)
    x = np.linspace(phi[0],1.05,1000)

    plt.plot(phi,M,'o',label = 'data')
    plt.plot(x,a*x,'r',label = 'fit')
    leg = plt.legend()	
    plt.title('y = 0.326x')
    plt.xlabel('$\\varphi$ [rad]')
    plt.ylabel('M [Nm]')
    plt.show()

    M2 = [el**2 for el in M]
    phi2 = [el**2 for el in phi]
    sigma = np.sqrt((1./len(M))*((sum(M2)/len(M2))/(sum(phi2)/len(phi2)) - a**2))
    print(u"\u00B1",sigma)
lingress()