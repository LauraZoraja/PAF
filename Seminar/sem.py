import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, T, Ex, Ey, Ez, Bx, By, Bz, mpolje = 'placeholder', epolje = 'placeholder', q = -1., m = 1., dt = 0.001):
        self.m = m
        self.q = q
        self.dt = dt
        self.T = T
        self.x = 0.
        self.y = 0.
        self.z = 0.
        self.t = 0.
        self.v = np.array((0.1,0.1,0.1))
        self.epolje = epolje
        self.mpolje = mpolje
        self.Ez = Ez if callable(Ez) else lambda t: Ez
        self.B = np.array((Bx,By,Bz(self.t)))
        self.E = np.array((Ex,Ey,self.Ez(self.t)))
        self.F = self.q * (self.E + np.cross(self.v, self.B))
        self.a = self.F / self.m
        if self.q == -1:
            self.cestica = 'elektron'
        elif self.q == 1:
            self.cestica = 'pozitron'


    def move_euler(self):
        self.v = self.v + self.a*self.dt
        self.x += self.v[0]*self.dt
        self.y += self.v[1]*self.dt
        self.z += self.v[2]*self.dt
        self.F = self.q * (self.E + np.cross(self.v, self.B))
        self.a = self.F / self.m
        self.t += self.dt
        if self.mpolje == 'promjenjivo':
            self.B += np.array((0.,0.,self.dt/10.))
        else:
            pass
    
        if self.epolje == 'promjenjivo':
            self.E += np.array((0.,0.,self.dt/100.))
        else:
            pass


    def euler(self):
        self.t = 0.
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
        self.listav = [self.v]
        self.listaa = [self.a]
        self.listat = [0.]
        while self.t < self.T:
            self.move_euler()
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaz.append(self.z)
            self.listav.append(self.v)
            self.listaa.append(self.a)
            self.listat.append(self.t)

    def plot(self,color = 'blue'):
        ax.plot(self.listax, self.listay, self.listaz, label = '{},{} magnetsko polje i {} elektricno polje'.format(self.cestica,self.mpolje,self.epolje), color = color)

    def plot_reset(self):
        self.x = self.listax[0]
        self.y = self.listay[0]
        self.z = self.listaz[0]
        self.v = self.listav[0]
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
        self.listav = [self.v]


def Bz1(t):
    return (1./10.)*t

def Bz2(t):
    return 1.

def Ez1(t):
    return (1./100.)*t

def Ez2(t):
    return 0.


#konstantno magnetsko, elektron
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_box_aspect([1,1,1])
h1 = Particle(30.,0.,0.,Ez2,0.,0.,Bz2,'konstantno', 'konstantno')
h2  = Particle(30.,0.,0.,Ez1,0.,0.,Bz2,'konstantno', 'promjenjivo')
h1.euler()
h2.euler()
h1.plot('blueviolet')
h2.plot('lightseagreen')  
ax.legend()
plt.show()

#samo za reference
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_box_aspect([1,1,1])
h2  = Particle(30.,0.,0.,Ez1,0.,0.,Bz2,'konstantno', 'promjenjivo')
h2.euler()
h2.plot('lightseagreen')
ax.legend()
plt.show()


#konstantno elektricno, usporedba + i - u promjenjivom magnetskom
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.set_box_aspect([1,1,1])
h4 = Particle(30.,0.,0.,Ez2,0.,0.,Bz2,'konstantno', 'konstantno')
h5  = Particle(30.,0.,0.,Ez2,0.,0.,Bz1,'promjenjivo', 'konstantno')
h6 = Particle(30.,0.,0.,Ez2,0.,0.,Bz1,'promjenjivo', 'konstantno', 1)
h4.euler()
h5.euler()
h6.euler()
h4.plot('blueviolet')
h5.plot('deeppink') 
h6.plot('lightseagreen') 
ax.legend()
plt.show()

#oba promjenjiva
fig = plt.figure()
ax = plt.axes(projection ='3d')
#ax.set_box_aspect([1,1,1])
h7 = Particle(30.,0.,0.,Ez1,0.,0.,Bz1,'promjenjivo', 'promjenjivo')
h8  = Particle(30.,0.,0.,Ez1,0.,0.,Bz1,'promjenjivo', 'promjenjivo', 1)
h7.euler()
h8.euler()
h7.plot('deeppink')
h8.plot('blueviolet') 
ax.legend()
plt.show()