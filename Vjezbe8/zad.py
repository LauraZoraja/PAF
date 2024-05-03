import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

class moving_particle:
    def __init__(self, t, vx, vy, vz, Ex, Ey, Ez, q = -1, x = 0, y = 0, z = 0, dt = 0.01, Bx = 0, By = 0,Bz = 1, m = 1):
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


    def move(self):
        self.v = self.v + self.a*self.dt
        self.x += self.v[0]*self.dt
        self.y += self.v[1]*self.dt
        self.z += self.v[2]*self.dt
        self.F = self.q * (self.E + np.cross(self.v, self.B))
        print(self.F)
        self.a = self.F / self.m
        self.T += self.dt

    def putanja(self):
        self.T = 0.
        self.listax = [self.x]
        self.listay = [self.y]
        self.listaz = [self.z]
        self.listav = [self.v]
        self.listaa = [self.a]
        self.listat = [0]
        while self.T < self.t:
            self.move()
            self.listax.append(self.x)
            self.listay.append(self.y)
            self.listaz.append(self.z)
            self.listav.append(self.v)
            self.listaa.append(self.a)
            self.listat.append(self.T)
        ##print(self.listav)

    def plot(self):
        ax.plot(self.listax, self.listay, self.listaz)
        
fig = plt.figure()
ax = plt.axes(projection ='3d')
h1 = moving_particle(20,0.1,0.1,0.1,0,0,0)
h2 = moving_particle(20,0.1,0.1,0.1,0,0,0,q=1)
h1.putanja()
h2.putanja()
h1.plot()
h2.plot()        
plt.show()
