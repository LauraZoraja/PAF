import matplotlib.pyplot as plt
import numpy as np

class otpor:
    def __init__(self,k,t,m,x = 0,v = 0,C1 = 0.12,C2 = 0.03):
        self.k = k
        self.t = t
        self.m = m
        self.x1 = x
        self.x2 = x
        self.x3 = x
        self.C1 = C1
        self.C2 = C2
        self.g = 9.81
        self.v1 = v
        self.v2 = v
        self.v3 = v
        self.F1 = -(self.C1)*(self.v1) - self.x1*self.k
        self.F2 = -(self.C1)*(self.v2) - (self.C2)*(self.v2)**2 - self.x2*self.k
        #self.F3 = -(self.C2)*(self.v3)**2 - self.x3*self.k
        self.listax1 = [self.x1]
        self.listax2 = [self.x2]
        #self.listax3 = [self.x3]
        self.listav1 = [self.v1]
        self.listav2 = [self.v2]
        #self.listav3 = [self.v3]
        self.listaF1 = [self.F1]
        self.listaF2 = [self.F2]
        #self.listaF3 = [self.F3]
        self.listaa1 = [self.F1/self.m]
        self.listaa2 = [self.F2/self.m]
        self.listat = [0.]

    def move_euler(self):
        
        self.v1 += (self.F1/self.m)*self.dt
        self.v2 += (self.F2/self.m)*self.dt
        #self.v3 += (self.F3/self.m)*self.dt
        self.x1 += self.v1*self.dt
        self.x2 += self.v2*self.dt
        #self.x3 += self.v3*self.dt
        self.F1 = -(self.C1)*self.v1 - self.x1*self.k
        self.F2 = -(self.C1)*self.v2 - (self.C2)*(self.v2)**2 - self.x2*self.k
        #self.F3 = -(self.C2)*(self.v3)**2 - self.x3*self.k

    def euler(self,dt = 0.01):
        self.T = 0
        self.dt = dt
        while self.T < self.t:
            self.T += self.dt
            self.move_euler()
            self.listav1.append(self.v1)
            self.listav2.append(self.v2)
           # self.listav3.append(self.v3)
            self.listax1.append(self.x1)
            self.listax2.append(self.x2)
           # self.listax3.append(self.x3)
            self.listaF1.append(self.F1)
            self.listaF2.append(self.F2)
           # self.listaF3.append(self.F3)
            self.listaa1.append(self.F1/self.m)
            self.listaa2.append(self.F2/self.m)
            self.listat.append(self.T)

    def plot(self):
        plt.subplot(3,1,1) #redak, stupac, prvi graf
        plt.plot(self.listat, self.listax1, 'o', markersize = 2, c = 'gray', label = 'F1')
        plt.plot(self.listat, self.listax2, 'o', markersize = 2, c = 'purple', label = 'F2')
        plt.xlabel("t [s]")
        plt.ylabel('x [m]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(3,1,2)
        plt.plot(self.listat, self.listav1, 'o', markersize = 2, c = 'gray', label = 'F1')
        plt.plot(self.listat, self.listav2, 'o', markersize = 2, c = 'purple', label = 'F2')
        plt.xlabel("t [s]")
        plt.ylabel('v [m/s]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(3,1,3)
        plt.plot(self.listat,self.listaa1, 'o', markersize = 2, c = 'gray', label = 'F1')
        plt.plot(self.listat,self.listaa2, 'o', markersize = 2, c = 'purple', label = 'F2')
        plt.xlabel("t [s]")
        plt.ylabel('a [m/s^2]')
        plt.grid()
        plt.tight_layout()
        plt.show()
        

h1 = otpor(5,5,0.1,1,0)
h1.euler()
h1.plot()


h2 = otpor(5,5,0.1,2.1,0)
h2.euler()
h2.plot()