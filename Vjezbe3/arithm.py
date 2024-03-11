def aritm(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
    import numpy as np
    a = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    x = float(sum(a))/len(a)

    listab = []
    for i in range(len(a)):
        b = float((a[i] - x)**2)
        listab.append(b)
    
    sigma = np.sqrt(float(sum(listab)/(len(a)*(len(a)-1))))

    #print('Aritmeticka sredina iznosi {}.'.format(x))
    #print('Standarna devijacija iznosi {}.'.format(sigma))

aritm(1,2,3,4,5,6,7,8,9,10)

def aritm_s_numpy(t1,t2,t3,t4,t5,t6,t7,t8,t9,t10):
    import numpy as np
    a = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]
    sigma2 = np.std(a) * np.sqrt(1./(len(a)-1))
    x = np.mean(a)
    print('Aritmeticka sredina iznosi {}.'.format(x))
    print('Standarna devijacija iznosi {}.'.format(sigma2))

aritm_s_numpy(1,2,3,4,5,6,7,8,9,10)