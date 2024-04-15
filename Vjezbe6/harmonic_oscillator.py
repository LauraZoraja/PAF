import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
    def __init__(self,k,m,xi = 0,vi = 0):
        self.k = k
        self.m = m
        self.xi = xi
        self.ai = -(k/m)*self.xi
        self.vi = vi
        self.listax = [self.xi]
        self.listav = [self.vi]
        self.listaa = [self.ai]
        self.listat = [0]
    def move(self):
        
        self.vi += self.ai*self.dt
        self.xi += self.vi*self.dt
        self.ai = -(self.k/self.m)*self.xi
        
        
        #self.vi = self.v2i
        #self.xi = self.x2i
        #self.ai = self.a2i

    def oscilate(self,t,dt = 0.01):
        self.t = t
        self.dt = dt
        self.T = 0
        while self.T < self.t:
            self.T += self.dt
            self.move()
            self.listav.append(self.vi)
            self.listax.append(self.xi)
            self.listaa.append(self.ai)
            self.listat.append(self.T)
        figure, axis = plt.subplots(3,1)
        axis[0].plot(self.listat,self.listax,'o',markersize = 1)
        axis[1].plot(self.listat,self.listav,'o',markersize = 1)
        axis[2].plot(self.listat,self.listaa,'o',markersize = 1)
        axis[0].set_xlabel('t [s]')
        axis[0].set_ylabel('a [m/$s^2$]')
        axis[1].set_xlabel('t [s]')
        axis[1].set_ylabel('v [m/s]')
        axis[2].set_xlabel('t [s]')
        axis[2].set_ylabel('x [m]')
        plt.tight_layout()


    #def plotx(self,t,dt = 0.01):
        #self.oscilate(t,dt)
        #self.t = t
        #self.dt = dt
        #plt.plot(self.listat,self.listax,'o',markersize = 3)
        #plt.title('Putanja cestice')
        #plt.xlabel('t [s]')
        #plt.ylabel('x [m]')
    

    def show(self):
        plt.show()

h1 = HarmonicOscillator(10,0.1,0.3,2)
h1.oscilate(2)
h1.oscilate(2,0.001)
h1.oscilate(2,0.05)
h1.show()