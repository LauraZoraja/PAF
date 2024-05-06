import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

class moving_particle:
    def __init__(self, t, vx, vy, vz, Ex, Ey, Ez, q = -1, x = 0, y = 0, z = 0, dt = 0.01, Bx = 0, By = 0,Bz = 1, m = 1, metoda = 'placeholder'):
        self.m = m
        self.q = q
        self.dt = dt
        self.t = t
        self.x = x
        self.y = y
        self.z = z
        self.v = np.array((vx,vy,vz))
        self.E = np.array((Ex,Ey,Ez))
        self.B = np.array((Bx,By,Bz))
        self.F = self.q * (self.E + np.cross(self.v, self.B))
        self.a = self.F / self.m
        if self.q == -1:
            self.cestica = 'elektron'
        elif self.q == 1:
            self.cestica = 'pozitron'
        self.metoda = metoda


    def move_euler(self):
        self.v = self.v + self.a*self.dt
        self.x += self.v[0]*self.dt
        self.y += self.v[1]*self.dt
        self.z += self.v[2]*self.dt
        self.F = self.q * (self.E + np.cross(self.v, self.B))
        self.a = self.F / self.m
        self.T += self.dt

    def euler(self, metoda = 'Euler'):
        self.T = 0.
        self.metoda = metoda
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
        self.listav = [self.v]
        self.listaa = [self.a]
        self.listat = [0]
        while self.T < self.t:
            self.move_euler()
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaz.append(self.z)
            self.listav.append(self.v)
            self.listaa.append(self.a)
            self.listat.append(self.T)

    def move_runge(self):
        self.k1v = (self.q * (self.E + np.cross(self.v, self.B)))*self.dt
        self.k1x = self.v*self.dt
        self.k2v = (self.q * (self.E + np.cross(self.v + self.k1v/2., self.B)))*self.dt
        self.k2x = (self.v + (self.k1v/2.))*self.dt
        self.k3v = (self.q * (self.E + np.cross(self.v + self.k2v/2., self.B)))*self.dt
        self.k3x = (self.v + (self.k2v/2.))*self.dt
        self.k4v = (self.q * (self.E + np.cross(self.v + self.k3v, self.B)))*self.dt
        self.k4x = (self.v + (self.k3v))*self.dt

        self.v += (1./6.)*(self.k1v + 2.*self.k2v + 2.*self.k3v + self.k4v)
        self.x += (1./6.)*(self.k1x[0] + 2.*self.k2x[0] + 2.*self.k3x[0] + self.k4x[0])
        self.y += (1./6.)*(self.k1x[1] + 2.*self.k2x[1] + 2.*self.k3x[1] + self.k4x[1])
        self.z += (1./6.)*(self.k1x[2] + 2.*self.k2x[2] + 2.*self.k3x[2] + self.k4x[2])

    def runge(self, dt = 0.01, metoda = 'Runge-Kutta'):
        self.metoda = metoda
        self.T = 0
        self.dt = dt
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
        self.listav = [self.v]
        while self.T < self.t:
            self.T += self.dt
            self.move_runge()
            self.listav.append(self.v)
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaz.append(self.z)

    def plot(self):
        ax.plot(self.listax, self.listay, self.listaz, label = '{},{}, dt = {}'.format(self.cestica,self.metoda,self.dt))

    def plot_reset(self):
        self.x = self.listax[0]
        self.y = self.listay[0]
        self.z = self.listaz[0]
        self.v = self.listav[0]
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
        self.listav = [self.v]
        
fig = plt.figure()
ax = plt.axes(projection ='3d')
h1 = moving_particle(20,0.1,0.1,0.1,0,0,0)
h2 = moving_particle(20,0.1,0.1,0.1,0,0,0,q=1)
h3 = moving_particle(20,0.1,0.1,0.1,0,0,0)
h1.euler()
h2.euler()
h1.plot()
h2.plot()  
ax.legend()
plt.show()

h1.plot_reset()
fig = plt.figure()
ax = plt.axes(projection ='3d')
h1.euler()
h3.runge()
h1.plot()
h3.plot()
ax.legend()
plt.show()