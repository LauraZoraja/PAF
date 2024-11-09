import matplotlib.pyplot as plt
import numpy as np

class otpor:
    def __init__(self,t,m,x,v,C1,C2,dt = 0.001):
        self.t = t
        self.m = m
        self.x1 = x
        self.x2 = x
        self.x3 = x
        self.C1 = C1
        self.C2 = C2
        self.g = 9.81
        self.dt = dt
        self.v1 = v
        self.v2 = v
        self.v3 = v
        self.F1 = -np.sign(self.v1)*(self.C1*self.m)*(self.v1)
        self.F2 = -np.sign(self.v2)*(self.C1*self.m)*(self.v2) - np.sign(self.v2)*(self.C2*self.m)*(self.v2)**2
        self.F3 = -np.sign(self.v3)*(self.C2*self.m)*(self.v3)**2
        self.listax1 = [self.x1]
        self.listax2 = [self.x2]
        self.listax3 = [self.x3]
        self.listav1 = [self.v1]
        self.listav2 = [self.v2]
        self.listav3 = [self.v3]
        self.listaF1 = [self.F1]
        self.listaF2 = [self.F2]
        self.listaF3 = [self.F3]
        self.listat = [0.]

    def move_euler(self):
        
        self.v1 += (self.F1/self.m)*self.dt
        self.v2 += (self.F2/self.m)*self.dt
        self.v3 += (self.F3/self.m)*self.dt
        self.x1 += self.v1*self.dt
        self.x2 += self.v2*self.dt
        self.x3 += self.v3*self.dt
        self.F1 = -np.sign(self.v1)*(self.C1*self.m)*(self.v1)
        self.F2 = -np.sign(self.v2)*(self.C1*self.m)*(self.v2) - np.sign(self.v2)*(self.C2*self.m)*(self.v2)**2
        self.F3 = -np.sign(self.v3)*(self.C2*self.m)*(self.v3)**2

    def euler(self,dt = 0.01):
        self.T = 0
        self.dt = dt
        while self.T < self.t:
            self.T += self.dt
            self.move_euler()
            self.listav1.append(self.v1)
            self.listav2.append(self.v2)
            self.listav3.append(self.v3)
            self.listax1.append(self.x1)
            self.listax2.append(self.x2)
            self.listax3.append(self.x3)
            self.listaF1.append(self.F1)
            self.listaF2.append(self.F2)
            self.listaF3.append(self.F3)
            self.listat.append(self.T)

    def plot1(self):
        plt.subplot(1,3,1) #jedan redak, tri stupca, prvi graf
        plt.plot(self.listav1,self.listaF1,markersize = 1)
        plt.xlabel("v [m/s]")
        plt.ylabel('F1 [N]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(1,3,2)
        plt.plot(self.listav2,self.listaF2,markersize = 1)
        plt.xlabel("v [m/s]")
        plt.ylabel('F2 [N]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(1,3,3)
        plt.plot(self.listav3,self.listaF3,markersize = 1)
        plt.xlabel("v [m/s]")
        plt.ylabel('F3 [N]')
        plt.grid()
        plt.tight_layout()
        plt.show()

    def plot2(self):
        plt.subplot(1,3,1) #jedan redak, tri stupca, prvi graf
        plt.plot(self.listav1,self.listat,markersize = 1)
        plt.xlabel("v [m/s] (F1)")
        plt.ylabel('t [s]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(1,3,2)
        plt.plot(self.listav2,self.listat,markersize = 1)
        plt.xlabel("v [m/s] (F2)")
        plt.ylabel('t [s]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(1,3,3)
        plt.plot(self.listav3,self.listat,markersize = 1)
        plt.xlabel("v [m/s] (F3)")
        plt.ylabel('t [s]')
        plt.grid()
        plt.tight_layout()
        plt.show()

    def plot3(self):
        plt.subplot(1,3,1) #jedan redak, tri stupca, prvi graf
        plt.plot(self.listav1,self.listat,markersize = 1)
        plt.xlabel("x [m] (F1)")
        plt.ylabel('t [s]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(1,3,2)
        plt.plot(self.listav2,self.listat,markersize = 1)
        plt.xlabel("x [m] (F2)")
        plt.ylabel('t [s]')
        plt.grid()
        plt.tight_layout()

        plt.subplot(1,3,3)
        plt.plot(self.listav3,self.listat,markersize = 1)
        plt.xlabel("x [m] (F3)")
        plt.ylabel('t [s]')
        plt.grid()
        plt.tight_layout()
        plt.show()
        

h1 = otpor(60,1,0,1,0.4,1.6)
h1.euler()
h1.plot1()
h1.plot2()
h1.plot3()


h2 = otpor(60,1,0,20,0.4,1.6)
h2.euler()
h2.plot1()
h2.plot2()
h2.plot3()