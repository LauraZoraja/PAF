def koordinate():
    T1_str = str(input('Unesite koordinate prve tocke u obliku (x,y): '))
    T2_str = str(input('Unesite koordinate druge tocke u obliku (x,y): '))
    T1_strip = T1_str.strip('(').strip(')')
    T2_strip = T2_str.strip('(').strip(')')
    x1 , y1 = T1_strip.split(',')
    x2 , y2 = T2_strip.split(',')
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
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
        
koordinate()