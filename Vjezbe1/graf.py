import numpy as np
import matplotlib.pyplot as plt

def graf():
    x1 = float(input('Unesite x koordinatu: '))
    y1 = float(input('Unesite y koordinatu: '))
    x2 = float(input('Unesite x koordinatu: '))
    y2 = float(input('Unesite y koordinatu: '))
    k = (y2 - y1)/(x2 - x1)
    l = - k*x1 +y1
    p = 'p'
    if l>0:
        p = '+'
    else:
        p = '-'

    if k == 1:
        if l != 0:
            print('y = x {} {}'.format(p,l))
        else:
            print('y = x')
    elif k!= 1 and k!= 0:
        if l != 0:
            print('y = {} x {} {}'.format(k,p,l))
        else:
            print('y = {} x'.format(k))
    else:
        if l != 0:
            print('y ={}'.format(l))
        else:
            print('y = {} {}'.format(p,k))

    listax = []
    listay = []

    for x in range(10):
        y = k*x + l
        listax.append(x)
        listay.append(y)
    pdf = 'keks'
    pdf = input('Zelite li spremiti graf kao PDF? (da = 1 / ne = 0): ')
    if pdf == 1:
        ime = str(input('Ime grafa: '))
        plt.plot(listax,listay)
        plt.savefig('{}.pdf'.format(ime))
    else:
        plt.plot(listax,listay)
        plt.show() 
graf()