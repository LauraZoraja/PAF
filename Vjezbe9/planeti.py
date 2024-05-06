import numpy as np
import matplotlib.pyplot as plt

import pdb
pdb.set_trace()
class planet:
    def __init__(self, t = 8765.808, ms = 1.989*10.**30., mz = 5.9742*10.**24., G =  6.67408*10.**(-11.), dt = 12., xz = 1.486*10.**11., vz = 29783.):
        self.t = t
        self.ms = ms
        self.mz = mz
        self.G = G
        self.dt = dt
        self.rz = np.array((xz,0.))
        self.rs = np.array((0.,0.))
        self.vz = np.array((0.,vz))
        self.vs = np.array((0.,0.))

    def move(self):
        #pdb.set_trace()
        razlika1 = self.rz - self.rs
        d = np.sqrt(razlika1[0]**2 + razlika1[1]**2)

        razlika2 = self.rs - self.rz
        d2 = np.sqrt(razlika2[0]**2 + razlika2[1]**2)

        self.az = (-self.G*self.mz/d**3)*(self.rs - self.rz)
        self.vz += self.az*self.dt
        self.rz += self.vz*self.dt

        self.asu = (-self.G*self.mz/d2**3)*(self.rz - self.rs)
        self.vs += self.asu*self.dt
        self.rs += self.vs*self.dt

    def godina(self):
        T = 0
        self.listarz = []
        self.listars = []
        self.listavz = []
        self.listavs = []
        self.listaaz = []
        self.listaasu = []
        while T <= self.t:
            self.move()
            self.listarz.append(self.rz)
            self.listars.append(self.rs)
            self.listavz.append(self.vz)
            self.listavs.append(self.vs)
            self.listaaz.append(self.az)
            self.listaasu.append(self.asu)

    def plot(self):
        plt.plot([x[0] for x in self.listarz],[x[1] for x in self.listarz],markersize = 1, label = 'dt = {},{}'.format(self.dt,self.metoda))
        plt.plot([x[0] for x in self.listars],[x[1] for x in self.listars],markersize = 1, label = 'dt = {},{}'.format(self.dt,self.metoda))
        plt.xlabel("x [m]")
        plt.ylabel('y [m]')
        plt.title("x-y graf")

h1 = planet()
h1.godina()
h1.plot()
h1.show()