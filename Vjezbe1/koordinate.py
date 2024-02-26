def koordinate():
    x1 = input('Unesite x koordinatu: ')
    x1 = float(x1)
    y1 = input('Unesite y koordinatu: ')
    y1 = float(y1)
    x2 = input('Unesite x koordinatu: ')
    x2 = float(x2)
    y2 = input('Unesite y koordinatu: ')
    y2 = float(y2)
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
    elif k!= 1:
        if l != 0:
            print('y = {}x {} {}'.format(k,p,l))
        else:
            print('y = {}x'.format(k))

        
koordinate()