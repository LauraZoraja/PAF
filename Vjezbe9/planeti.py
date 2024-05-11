import numpy as np
import matplotlib.pyplot as plt

import pdb
#pdb.set_trace()
class planet:

    def __init__(self, t = 365.24 * 24. * 3600., ms = 1.989*10.**30., mz = 5.9742*10.**24., G =  6.67408*10.**(-11.), dt = 86400., xz = 1.486*10.**11., vz = 29783.):
        self.t = t
        self.ms = ms
        self.mz = mz
        self.G = G
        self.dt = dt
        self.rz = np.array((xz,0.))
        self.rs = np.array((0.,0.))
        self.vz = np.array((0.,vz))
        self.vs = np.array((0.,0.))
        self.dz = (self.rz[0]**2. + self.rz[1]**2.)**0.5
        self.listarzx = [self.rz[0]]
        self.listarzy = [self.rz[1]]
        self.az = (-self.G*self.mz/(self.dz**3.))*(self.rz)

    def move(self):
        #pdb.set_trace()
        self.rz += self.vz*self.dt
        self.vz += self.az*self.dt
        self.dz = (self.rz[0]**2. + self.rz[1]**2.)**0.5
        self.az = (-self.G*self.mz/(self.dz**3.))*(self.rz)

    def godina(self):
        T = 0
        while T < self.t:
            self.move()
            self.listarzx.append(self.rz[0])
            self.listarzy.append(self.rz[1])
            T += self.dt
            #pdb.set_trace()
            print(self.az,self.vz,self.rz)
        #print(self.listarzx,self.listarzy)

    def plot(self):
        plt.plot(self.listarzx, self.listarzy)
        plt.scatter(0, 0)
        plt.xlabel("x [m]")
        plt.ylabel('y [m]')
        plt.title("x-y graf")
        plt.show()

h1 = planet()
h1.godina()
h1.plot()