def jednoliko_gibanje_analiticki(F,m,t,v0,x0):
    import matplotlib.pyplot as plt
    import numpy as np

    t2 = int(round(t))
    if t2<t:
        t2 += 1
    else:
        t2 = t2
    listaa = []
    listax = []
    listav = []
    for T in range(0,t2+1):
        a = F/m
        x = x0 + v0*T + (a*T**2)/2
        v = v0 + a*T
        listaa.append(a)
        listax.append(x)
        listav.append(v)

    figure, axis = plt.subplots(3,1)
    axis[0].plot(list(range(0,t2+1)),listaa,'r')
    axis[1].plot(list(range(0,t2+1)),listav,'b')
    axis[2].plot(list(range(0,t2+1)),listax,'g')
    axis[0].set_xlabel('t [s]')
    axis[0].set_ylabel('a [m/$s^2$]')
    axis[1].set_xlabel('t [s]')
    axis[1].set_ylabel('v [m/s]')
    axis[2].set_xlabel('t [s]')
    axis[2].set_ylabel('x [m]')
    plt.tight_layout()
    plt.show()

def kosi_hitac_analiticki(v0,kut,t):
    import matplotlib.pyplot as plt
    import numpy as np

    g = 9.81
    kutr = np.radians(kut)
    t2 = int(round(t))
    if t2<t:
        t2 += 1
    else:
        t2 = t2
    listax = []
    listay = []
    for T in range(0,t2+1):
        x = v0*np.cos(kutr)*T
        y = v0*np.sin(kutr)*T - 0.5*g*T**2
        listax.append(x)
        listay.append(y)

    figure, axis = plt.subplots(3,1)
    axis[0].plot(listay,listax,'r')
    axis[1].plot(list(range(0,t2+1)),listax,'b')
    axis[2].plot(list(range(0,t2+1)),listay,'g')
    axis[0].set_xlabel('y [m]')
    axis[0].set_ylabel('x [m]')
    axis[1].set_xlabel('t [s]')
    axis[1].set_ylabel('x [m]')
    axis[2].set_xlabel('t [s]')
    axis[2].set_ylabel('y [m]')
    plt.tight_layout()
    plt.show()

def jednoliko_gibanje(F,m,t,dt=0.01):
    import matplotlib.pyplot as plt
    import numpy as np

    listaa = []
    listax = []
    listav = []
    x_i = 0
    v_i = 0
    for tn in np.arange(0,t,dt):
        a = F/m
        v_2i = v_i + a*dt
        x_2i = x_i + v_i*dt
        listaa.append(a)
        listax.append(x_2i)
        listav.append(v_2i)
        v_i = v_2i
        x_i = x_2i

    figure, axis = plt.subplots(3,1)
    axis[0].plot(list(np.arange(0,t,dt)),listaa,'r')
    axis[1].plot(list(np.arange(0,t,dt)),listav,'b')
    axis[2].plot(list(np.arange(0,t,dt)),listax,'g')
    axis[0].set_xlabel('t [s]')
    axis[0].set_ylabel('a [m/$s^2$]')
    axis[1].set_xlabel('t [s]')
    axis[1].set_ylabel('v [m/s]')
    axis[2].set_xlabel('t [s]')
    axis[2].set_ylabel('x [m]')
    plt.tight_layout()
    plt.show()


def kosi_hitac(v0,kut,t,dt=0.01):
    import matplotlib.pyplot as plt
    import numpy as np

    kutr = np.radians(kut)
    listax = []
    listavx = []
    listavy = []
    listay = []
    x_i = 0
    y_i = 0
    vx_i = v0*np.cos(kutr)
    vy_i = v0*np.sin(kutr)
    ax = 0
    ay = -9.81
    for T in np.arange(0,t,dt):
        vx_2i = vx_i + ax*dt
        vy_2i = vy_i + ay*dt
        x_2i = x_i + vx_2i*dt
        y_2i = y_i + vy_2i*dt
        listax.append(x_2i)
        listay.append(y_2i)
        x_i = x_2i
        y_i = y_2i
        vx_i = vx_2i
        vy_i = vy_2i

    figure, axis = plt.subplots(3,1)
    axis[0].plot(listax,listay,'r')
    axis[1].plot(list(np.arange(0,t,dt)),listax,'b')
    axis[2].plot(list(np.arange(0,t,dt)),listay,'g')
    axis[0].set_xlabel('x [m]')
    axis[0].set_ylabel('y [m]')
    axis[1].set_xlabel('t [s]')
    axis[1].set_ylabel('x [m]')
    axis[2].set_xlabel('t [s]')
    axis[2].set_ylabel('y [m]')
    plt.tight_layout()
    plt.show()

jednoliko_gibanje(30,2,10)
kosi_hitac(50,45,10)